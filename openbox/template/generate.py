import sys
import re
from subprocess import call 

out_name = 'rc.xml'

if __name__=="__main__":
    other_files = {}

    try:
        base = open('base.xml', 'r').read() # throws if file not found

        open_braces = []
        closed_braces = []
        found_open_brace = False
        found_closed_brace = False
        for index, letter in enumerate(base):
            if letter == '{':
                if found_open_brace == True:
                    open_braces.append(index)
                found_open_brace = True
            else:
                found_open_brace = False

            if letter == '}':
                if found_closed_brace == True:
                    closed_braces.append(index)
                found_closed_brace = True
            else:
                found_closed_brace = False
        
        if len(open_braces)==len(closed_braces):
            for index, position in reversed(list(enumerate(open_braces))):
                key = base[ open_braces[index]+1 : closed_braces[index]-1 ]
                print('Found: ' + key)
                start = base[:open_braces[index]-1]
                end = base[closed_braces[index]+1:]   
                
                base = start + open(key+'.xml', 'r').read() + end
            
            print('Writing to: ' + out_name)
            out_file = open('../'+out_name, 'w')
            out_file.write(base)
            out_file.close()
            print('Done, reconfiguring openbox')
            call("openbox --reconfigure", shell=True)


    except Exception as e:
        print(e)