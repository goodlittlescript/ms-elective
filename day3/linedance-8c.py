import os

line = [
    ".",
    ".",
    ".",
    ".",
    ".",
    ".",
    ".",
    ".",
    "."
]

os.system('clear')
print("location 1")
location = 1
for index, char in enumerate(line):
    if index == location:
        print("X")
    else:
        print(char)
input()

os.system('clear')
print("location 2")
location = 2
for index, char in enumerate(line):
    if index == location:
        print("X")
    else:
        print(char)
input()

os.system('clear')
print("location 3")
location = 3
for index, char in enumerate(line):
    if index == location:
        print("X")
    else:
        print(char)
input()
