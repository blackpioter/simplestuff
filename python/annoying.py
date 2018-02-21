#!/usr/local/bin/python3
print('case 1')
name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

print('=============================')
print('case 2')
name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
