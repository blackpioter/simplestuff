#!/usr/local/bin/python3
import re
import sys


def regex_strip(text, chars=' '):
    result = re.search('^[{s}]*(.*?)[{s}]*$'.format(s=chars), text).group(1)
    print('\'' + result + '\'')


if len(sys.argv) == 1:
    print("Usage: " +
          sys.argv[0] +
          " string_to_strip" +
          " string_of_chars_to_strip")
    exit()
elif len(sys.argv) < 3:
    text = sys.argv[1]
    chars = ' '
else:
    text = sys.argv[1]
    chars = sys.argv[2]

regex_strip(text, chars)
