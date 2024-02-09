import os
import curses
import time
import sys


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
}

instructions = "enter command (h:left j:down k:up l:right q:quit)"


def main(stdscr):
    start = time.time()
    max_y = len(lines)
    max_x = len(lines[0])

    y_location = 0
    for line in lines:
        stdscr.addstr(y_location, 0, line)
        y_location += 1
    stdscr.addstr(max_y, 0, instructions)

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

        y_location = bound_location(y_location, 0, max_y)
        x_location = bound_location(x_location, 0, max_x)

        curr_chr = chr(stdscr.inch(y_location, x_location))
        if curr_chr == ".":
            # Bounce back to previous location
            y_location, x_location = y_curr, x_curr
        if curr_chr == "*":
            # Win condition!
            return

        stdscr.move(y_location, x_location)
        stdscr.refresh()


curses.wrapper(main)
print("You won!")
