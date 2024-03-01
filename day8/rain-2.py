import curses
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


keymap = {
    "h": "left",
    "l": "right",
    " ": "drop",
    "q": "quit",
}


def main(stdscr):
    stdscr.nodelay(True)
    max_y, max_x = stdscr.getmaxyx()

    now = 0
    y_location = 0
    x_location = 0
    raindrops = []

    debug = (
        f"now: {now} ({y_location:.0f}, {x_location:.0f}) raindrops: {len(raindrops)}"
    )
    stdscr.addstr(max_y - 1, 0, debug.ljust(max_x - 1, " "))
    stdscr.move(int(y_location), int(x_location))
    stdscr.refresh()

    while True:
        time.sleep(0.1)
        try:
            key = stdscr.getkey()
        except Exception:
            key = ""
        cmd = keymap.get(key, "unknown")

        if cmd == "left":
            x_location -= 1
        if cmd == "right":
            x_location += 1
        if cmd == "quit":
            exit()
        if cmd == "unknown":
            pass

        y_location = bound_location(y_location, 0, max_y)
        x_location = bound_location(x_location, 0, max_x)
        now += 1

        if cmd == "drop":
            raindrop = [y_location, x_location]
            raindrops.append(raindrop)
        for raindrop_y, raindrop_x in raindrops:
            stdscr.addstr(raindrop_y, raindrop_x, ".")

        debug = f"now: {now} ({y_location:.0f}, {x_location:.0f}) raindrops: {len(raindrops)}"
        stdscr.addstr(max_y - 1, 0, debug.ljust(max_x - 1, " "))
        stdscr.move(int(y_location), int(x_location))
        stdscr.refresh()


curses.wrapper(main)
