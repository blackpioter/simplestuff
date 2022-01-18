#!/usr/local/bin/python3


def comma_code(arr):
    if len(arr) >= 2:
        arr[-1] = 'and ' + arr[-1]
        print(', '.join(arr))
    else:
        print("Array is too short")


spam = ['apples', 'bananas', 'tofu', 'cats']
comma_code(spam)
