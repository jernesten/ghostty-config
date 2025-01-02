#!/bin/python3

file = open('/home/jernst/.config/ghostty/ghostty-config/config', 'r')
read = file.readlines()
modified = []
final = []

# read the file line by line ignore all empty lines and append all the lines that begins with 'keybinds' to the list 'modified'

for line in read:
    if line != '\n':
        modified.append(line[:-1])

file.close()

for row in modified:
    if row.startswith('keybind'):
        comando = row.split('=')[-1]
        ccap = comando.capitalize()
        atajo = row.split('=')[-2]
        aupper = atajo.upper()
        KeyBind = str('- ' + ccap + ' = ' + aupper)
        final.append(KeyBind)

print('\n################ KEYBINDINGS ################\n')

for keybind in final:
    print(keybind)

print('\n#################### END ####################\n')

