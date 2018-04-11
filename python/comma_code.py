#!/usr/local/bin/python3


def comma_code(arr):
    arr[-1] = 'and ' + arr[-1]
    print(', '.join(arr))


spam = ['apples', 'bananas', 'tofu', 'cats']
comma_code(spam)
