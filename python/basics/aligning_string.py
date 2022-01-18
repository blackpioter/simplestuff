#!/usr/local/bin/python3

print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello World'.rjust(20))
print('Hello'.ljust(10))
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20))
print('Hello'.center(20, '='))


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
