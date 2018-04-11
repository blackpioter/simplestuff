#!/usr/local/bin/python3
import copy


def eggs(someParameter):
    someParameter.append('Hello')


spam = [1, 2, 3]
# Calling function on list
# This will cause to change in list passed to function
print(spam)
eggs(spam)
print(spam)

print()

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)
