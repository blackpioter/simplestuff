#!/usr/local/bin/python3
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


result = 0
while result != 1:
    print("Enter number:")
    try:
        num = int(input())
    except ValueError:
        print("You must enter integer")
        print("")
        continue
    result = collatz(num)
    print("")
