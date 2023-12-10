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

def render(line, location):
    os.system('clear')
    for index, char in enumerate(line):
        if index == location:
            print("X")
        else:
            print(char)
    input()

render(line, 1)
render(line, 2)
render(line, 3)
render(line, 4)
render(line, 5)
render(line, 6)
render(line, 7)
