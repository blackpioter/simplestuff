#!/usr/local/bin/python3

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    while True:
        print('Hello Joe, what is the password?')
        password = input()
        if password == 'swordfish':
            break
    break
print('Access granted')
