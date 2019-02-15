from wmctrl import Window
import os
import math
import subprocess

name_length = 20
name_center = True
active_color = '%{F#ffffff}'
background_color = '%{F#666666}'

def get_current_desktop():
    out = subprocess.check_output('wmctrl -d', shell=True)
    for line in out.splitlines():
        spl = line.split('*')
        if len(spl)>1:
            return int(spl[0].strip())




def get_name(win):
    if win.desktop==-1 or win.desktop!=current_desktop:
        return None

        
    active_win = Window.get_active()
    name = win.wm_name
    is_active = active_win and active_win.id == win.id

    # Subtract 3 for ellipsis 
    if len(name) > name_length-3:
        name = name[:name_length-3] + '...'
    else:
        remaining = name_length-len(name)
        if name_center:
            if remaining%2 == 0:
                name = ' '*(remaining/2) + name + ' '*(remaining/2)
            else:    
                name = ' '*int(math.floor(remaining/2.0)) + name + ' '*int(math.ceil(remaining/2.0))
        else:
            name = name + ''*remaining
    

    return (
        '%{A1:wmctrl -i -a '+win.id+':}' +
        (is_active and active_color or background_color) +
        "[ {} ]".format(name) +
        '%{F-}' +
        '%{A}'
    )
    

current_desktop = get_current_desktop()
windows_list = Window.list()
if len(windows_list)>0:
    names = [get_name(win) for win in windows_list]
    names_formatted = "".join([name for name in names if name is not None])
    print(names_formatted)