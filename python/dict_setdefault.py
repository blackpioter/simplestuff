#!/usr/local/bin/python3

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}

print(eggs)

eggs.setdefault('color', 'black')
print(eggs)

eggs.setdefault('color', 'orange')
print(eggs)
