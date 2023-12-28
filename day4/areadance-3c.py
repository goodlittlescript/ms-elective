import os
import time
import sys

lines = [
    list("#########"),
    list("#       #"),
    list("#       #"),
    list("#       #"),
    list("#       #"),
    list("#       #"),
    list("#       #"),
    list("#       #"),
    list("#########"),
]

locations = [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [5, 5],
    [6, 6],
    [7, 7],
    [6, 6],
    [5, 5],
    [4, 4],
    [3, 3],
    [2, 2],
]


def render(lines, location):
    os.system("clear")
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if x == location[0] and y == location[1]:
                sys.stdout.write("X")
            else:
                sys.stdout.write(char)
        sys.stdout.write("\n")


for _ in range(0, 3):
    for location in locations:
        render(lines, location)
        time.sleep(0.1)
render(lines, [1, 1])
