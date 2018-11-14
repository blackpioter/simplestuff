#!/usr/local/bin/python3
import os


txt = 'hello.txt'

file = open(txt)
content_lines = file.readlines()  # get file as lines in array
print(content_lines)
file.close()


file2 = open(txt)
content = file2.read()  # read whole file
print(content)
file2.close()
