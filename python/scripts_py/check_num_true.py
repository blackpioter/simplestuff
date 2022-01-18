#!/usr/local/bin/python3
def is_number(n):
    try:
        float(n)
        '''
        Type-casting the string to `float`.
        If string is not a valid `float`,
        it'll raise `ValueError` exception
        '''
    except ValueError:
        return False
    return True


def is_true(val):
    if val:
        return True
    else:
        return False


arr = [-2, -2.0, 0.0, 0, '']
print("Items: " + str(arr) + "\n")

for item in arr:
    print("Item " + str(item) + " is number? : " + str(is_number(item)))

print('\n===================\n')

for item in arr:
    print("Item " + str(item) + " is True? : " + str(is_true(item)))
