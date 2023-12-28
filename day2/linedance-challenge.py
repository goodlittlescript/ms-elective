import os
import time

lines = [
    # Make the character change when going forward/backward
    # forward  ">"
    # backward "<"
    ".>.......",
    "..>......",
    "...>.....",
    "....>....",
    ".....>...",
    "......>..",
    ".......<.",
    "......<..",
    ".....<...",
    "....<....",
    "...<.....",
    "..<......",
]


def render(line):
    os.system("clear")
    print(line)


for _ in range(0, 3):
    for line in lines:
        # Turn this into a function
        render(line)
        time.sleep(0.1)

render(line)
