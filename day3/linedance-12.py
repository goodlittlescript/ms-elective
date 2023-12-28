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
    location += offset

    if location >= 7:
        offset = -1
    elif location <= 1:
        offset = 1

    time.sleep(0.1)
