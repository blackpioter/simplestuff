#!/usr/local/bin/python3

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')

for i in range(len(lines)):     # loop through all indexes in the "lines" list
    if lines[i] != '':
        lines[i] = '* ' + lines[i]  # add star to each string in "lines" list

text = '\n'.join(lines)
pyperclip.copy(text)
