#!/usr/local/bin/python3
import re
# regex matching
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4252')
print(mo.group())  # show whole match
print(mo.group(1))  # show first group

# regex matching with pipe
batRegex = re.compile(r'Bat(man|mobile|copter)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))  # show which group applied

# Failing a regex
batRegex = re.compile(r'Bat(man|mobile|copter)')
mo = batRegex.search('Batcycle lost a wheel')
print("If not found should be equal none: " + str(mo is None))  # Simple output
