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
    next_y = random.randint(1, 7)
    next_x = random.randint(1, 7)
    return [next_y, next_x]

def render(lines, locatio):
    os.system("clear")
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if x == location[0] and y == location[1]:
                sys.stdout.write("X")
            else:
                sys.stdout.write(char)
        sys.stdout.write("\n")

target = [5,5]
for _ in range(0,20):
    location = pick_next_location()
    render(lines, location)
    time.sleep(0.1)

    if location == target:
        print("you win!")
        exit(0)

print("you lost!")