#!/usr/local/bin/python3
name = ''
while not name:
    print('Enter your name')
    name = input()
print('How many guests will you have?')
numOfGuests = input()
if numOfGuests:
    print("You've invited " + str(numOfGuests) + ' guests')
print('Done')
