import os
import time
import sys
import random

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

def pick_next_location():
    next_y = random.randint(0, 7)
    next_x = random.randint(0, 7)
    return [next_y, next_x]

def render(lines, location):
    os.system("clear")
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if x == location[0] and y == location[1]:
                sys.stdout.write("X")
            else:
                sys.stdout.write(char)
        sys.stdout.write("\n")

for _ in range(0,3):
    location = pick_next_location()
    render(lines, location)
    time.sleep(0.1)
