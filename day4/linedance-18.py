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


line = "........"

keymap = {
    "h": "left",
    "l": "right",
    "q": "quit",
}

instructions = "enter command (h:left l:right q:quit)"


def main(stdscr):
    stdscr.addstr(0, 0, line)
    stdscr.addstr(1, 0, instructions)

    location = 5
    stdscr.addstr(0, location, " ")
    stdscr.move(0, location)
    stdscr.refresh()

    while True:
        key = stdscr.getkey()
        cmd = keymap.get(key, "unknown")

        if cmd == "left":
            location -= 1
        if cmd == "right":
            location += 1
        if cmd == "quit":
            break
        if cmd == "unknown":
            pass

        location = bound_location(location, 0, len(line))

        stdscr.addstr(0, location, " ")
        stdscr.move(0, location)
        stdscr.refresh()


curses.wrapper(main)
