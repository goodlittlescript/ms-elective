import os
import time
import sys

def render(maze, x, y):
    os.system('clear')
    print("Actions: h (right) j (down) k (up) l (left) q (quit)")
    for y_index, line in enumerate(maze):
        for x_index, char in enumerate(line):
            if x_index == x and y_index == y:
                sys.stdout.write("X")
            else:
                sys.stdout.write(char)
        sys.stdout.write("\n")
    sys.stdout.write("\n")
#############################################################################

maze = [
    list(":::::::::"),
    list(":.......:"),
    list(":.......:"),
    list(":.:::::.:"),
    list(":.::....:"),
    list("::::.::::"),
    list(":::::::::"),
]

x = 1
y = 1
render(maze, x, y)

while True:
    user_input = sys.stdin.read(1)

    new_x = x
    new_y = y
    if user_input == "l":
        new_x += 1
    if user_input == "h":
        new_x -= 1
    if user_input == "j":
        new_y += 1
    if user_input == "k":
        new_y -= 1
    if user_input == "q":
        print("Thanks for playing!")
        exit()

    if maze[new_y][new_x] == ".":
        x = new_x
        y = new_y

    render(maze, x, y)
