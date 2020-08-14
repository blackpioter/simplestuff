#!/usr/local/bin/python3
import pprint

file = open("rj.txt", "r")
count = {}

for character in file.read().upper():
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
file.close()
