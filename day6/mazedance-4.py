import os
import time
import sys


def render(line, location):
    os.system("clear")
    print("Actions: h (right) l (left) q (quit)")
    for index, char in enumerate(line):
        if index == location:
            sys.stdout.write("X")
        else:
            sys.stdout.write(char)
    sys.stdout.write("\n")


line = [":", ".", ".", ".", ".", ".", ".", ".", ":"]

location = 1
render(line, location)

while True:
    user_input = sys.stdin.read(1)

    new_location = location
    if user_input == "l":
        new_location += 1
    if user_input == "h":
        new_location -= 1
    if user_input == "q":
        print("Thanks for playing!")
        exit()

    if line[new_location] == ".":
        location = new_location

    render(line, location)
