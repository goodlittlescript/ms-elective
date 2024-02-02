import os
import curses


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


lines = [
    "........",
    "........",
    "........",
    "........",
    "........",
]

keymap = {
    "h": "left",
    "j": "down",
    "k": "up",
    "l": "right",
    "q": "quit",
}

instructions = "enter command (h:left j:down k:up l:right q:quit)"


def main(stdscr):
    y_location = 0
    for line in lines:
        stdscr.addstr(y_location, 0, line)
        y_location += 1
    stdscr.addstr(y_location, 0, instructions)

    y_location = 0
    x_location = 5

    stdscr.addstr(y_location, x_location, " ")
    stdscr.move(y_location, x_location)
    stdscr.refresh()

    while True:
        key = stdscr.getkey()
        cmd = keymap.get(key, "unknown")

        if cmd == "left":
            x_location -= 1
        if cmd == "right":
            x_location += 1
        if cmd == "up":
            y_location -= 1
        if cmd == "down":
            y_location += 1
        if cmd == "quit":
            break
        if cmd == "unknown":
            pass

        x_location = bound_location(x_location, 0, len(lines[0]))
        y_location = bound_location(y_location, 0, len(lines))

        stdscr.addstr(y_location, x_location, " ")
        stdscr.move(y_location, x_location)
        stdscr.refresh()


curses.wrapper(main)
