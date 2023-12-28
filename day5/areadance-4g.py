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


def render(lines, location):
    os.system("clear")
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if x == location[0] and y == location[1]:
                sys.stdout.write("X")
            else:
                sys.stdout.write(char)
        sys.stdout.write("\n")


location = [1, 1]
offset = [1, 1]
for _ in range(0, 20):
    render(lines, location)
    time.sleep(0.1)

    new_location = [
        location[0] + offset[0],
        location[1] + offset[1],
    ]

    char = lines[new_location[0]][new_location[1]]
    if char == "#":
        offset[0] *= -1
        offset[1] *= -1
    else:
        location = new_location
