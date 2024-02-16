import os
import curses
import sys
import time


# Bounds the location if it leaves the specified range.
#
# Note the range is [lower,upper) meaning it includes the
# lower value but only goes "up to" the upper value.
def bound_location(location, lower, upper):
    if location >= upper:
        return upper - 1
    elif location < lower:
        return lower
    else:
        return location


def load_maze(filename):
    with open(filename) as f:
        maze = f.read()
        lines = maze.split("\n")
        return lines


command_name, maze_file = sys.argv
lines = load_maze(maze_file)

keymap = {
    "h": "left",
    "j": "down",
    "k": "up",
    "l": "right",
    "q": "quit",
    "i": "insert",
    chr(27): "move",
}


def main(stdscr):
    mode = "move"
    max_y, max_x = stdscr.getmaxyx()

    y_location = 0
    for line in lines:
        stdscr.addstr(y_location, 0, line)
        y_location += 1

    y_location = 0
    x_location = 1

    stdscr.move(y_location, x_location)
    stdscr.refresh()

    while True:
        key = stdscr.getkey()
        cmd = keymap.get(key, "unknown")

        y_curr, x_curr = stdscr.getyx()

        if cmd == "left":
            x_location -= 1
        if cmd == "right":
            x_location += 1
        if cmd == "up":
            y_location -= 1
        if cmd == "down":
            y_location += 1
        if cmd == "quit":
            exit()
        if cmd == "unknown":
            pass
        if cmd == "insert":
            mode = "insert"
        if cmd == "move":
            mode = "move"

        y_location = bound_location(y_location, 0, max_y)
        x_location = bound_location(x_location, 0, max_x)

        # debug line
        stdscr.addstr(
            max_y - 1,
            0,
            f"{y_location}/{x_location} {mode} {repr(key)} {ord(key) if len(key) == 1 else ''}".ljust(
                max_x - 1, " "
            ),
        )

        if mode == "insert":
            stdscr.addstr(y_location, x_location, ".")

        stdscr.move(y_location, x_location)
        stdscr.refresh()


curses.wrapper(main)
