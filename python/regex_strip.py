#!/usr/local/bin/python3
import re
import sys


def regex_strip(inp, toRemove=' '):
    out = inp
    for char in toRemove:
        regex_start = r"^" + re.escape(char)
        regex_end = re.escape(char) + r"$"

        out = re.sub(regex_start, '', out)
        out = re.sub(regex_end, '', out)
    print(out)


if len(sys.argv) == 1:
    print("Usage: " +
          sys.argv[0] +
          " string_to_strip" +
          " string_of_chars_to_strip")
    exit()
elif len(sys.argv) < 3:
    inp = sys.argv[1]
    chars = ' '
else:
    inp = sys.argv[1]
    chars = sys.argv[2]

regex_strip(inp, chars)
