#!/usr/local/bin/python3


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


print(grid)
print()

print('-----------------------')

# original
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(grid[i][j], end='')
    print()

print('-----------------------')

# rotated 90 clockwise
for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j], end='')
    print()
