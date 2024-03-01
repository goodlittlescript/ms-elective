import curses
import time
from scene import Scene

keymap = {
    "h": "left",
    "l": "right",
    " ": "drop",
    "q": "quit",
    "KEY_RESIZE": "resize",
}


def main(stdscr):
    stdscr.nodelay(True)
    scene = Scene()
    scene.refresh(stdscr)

    while True:
        time.sleep(0.1)
        try:
            key = stdscr.getkey()
        except Exception:
            key = ""
        cmd = keymap.get(key, "unknown")

        if cmd == "left":
            scene.cloud.move_left()
        if cmd == "right":
            scene.cloud.move_right()
        if cmd == "resize":
            stdscr.clear()
        if cmd == "quit":
            exit()
        if cmd == "unknown":
            pass

        if cmd == "drop":
            scene.add_raindrop()
        scene.refresh(stdscr)


curses.wrapper(main)
