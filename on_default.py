import os

list_dirs = []
for currentdir, dirs, files in os.walk('../tap_tap_dash'):
    if '.git' not in currentdir and 'levels' not in currentdir:
        list_dirs.append((currentdir, dirs, files))


txt = list(map(lambda x: tuple(x.split('=')), open('default.txt', mode='r').read().split()))
for el_txt in txt:
    for el_list_dirs in list_dirs:
        if  el_txt[0] in el_list_dirs[-1]:
            with open(f'{el_list_dirs[0]}/{el_txt[0]}', 'w') as txt:
                txt.write(el_txt[1])
                txt.close()