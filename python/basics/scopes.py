#!/usr/local/bin/python3
def spam():
    eggs = 99
    bacon()
    print(eggs)


def bacon():
    ham = 101
    eggs = 0


def spam2():
    global eggs
    eggs = 'spam'


eggs = 'global'
spam()
spam2()
print(eggs)
