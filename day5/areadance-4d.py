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

location = [1,1]
for _ in range(0,20):
    render(lines, location)
    time.sleep(0.1)

    location[0] += 1
    char = lines[location[0]][location[1]]
    if char == "#":
        print("hit a wall!")
        break
