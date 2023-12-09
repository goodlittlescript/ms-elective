import os
import time

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

locations = [
    1,2,3,4,5,6,7
]

def render(line, location):
    os.system('clear')
    for index, char in enumerate(line):
        if index == location:
            print("X")
        else:
            print(char)
    time.sleep(0.1)

for location in locations:
    render(line, location)
