import os
import time
import sys

line = [":", ".", ".", ".", ".", ".", ".", ".", ":"]


def render(line, location):
    os.system("clear")
    for index, char in enumerate(line):
        if index == location:
            sys.stdout.write("X")
        else:
            sys.stdout.write(char)
    sys.stdout.write("\n")


location = 1
offset = 1
for _ in range(0, 40):
    render(line, location)

    print(f"offset: {offset}")
    next_location = location + offset

    if line[next_location] == ":":
        offset *= -1
        next_location = location + offset

    location = next_location

    time.sleep(0.1)
