#!/usr/local/bin/python3
import os


print(os.getcwd())
print(os.path.abspath('.'))  # provide absolute path

print(os.path.isabs('.'))  # check if provided path is absolute
print(os.path.isabs(os.path.abspath('.')))

path = '/usr/local/bin/ansible'
path_dir = os.path.dirname(path)

print(os.path.relpath(path, '.'))  # show relation between paths
print(os.path.basename(path))  # only basename / filename
print(os.path.dirname(path))  # only dirname
print(os.path.split(path))  # split into dirname and basename - tuple
print(path.split(os.sep))  # split path by OS separator

print(os.path.getsize(path))  # show size of file in bytes
print(os.listdir(path_dir))  # list files in dir

totalSize = 0
for item in os.listdir(path_dir):
    if os.path.isdir(os.path.join(path_dir, item)):
        # print only if item is a dir
        print(os.path.join(path_dir, item))
    totalSize += os.path.getsize(os.path.join(path_dir, item))
print("Total Size of files in " + path_dir + ": " + str(totalSize))

print(os.path.exists(path))
print(os.path.exists('C:\\'))
