import os
import time
import sys

line = [":", ".", ".", ".", ".", ".", ".", ".", ":"]

locations = [1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1]


def render(line, location):
    os.system("clear")
    for index, char in enumerate(line):
        if index == location:
            sys.stdout.write("X")
        else:
            sys.stdout.write(char)
    sys.stdout.write("\n")


for location in locations:
    render(line, location)
    time.sleep(0.1)
