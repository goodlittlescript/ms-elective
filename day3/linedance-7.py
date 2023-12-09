import os
import time

lines = [
    ".X.......",
    "..X......",
    "...X.....",
    "....X....",
    ".....X...",
    "......X..",
    ".......X.",
    "......X..",
    ".....X...",
    "....X....",
    "...X.....",
    "..X......",
]

def render(line):
    os.system('clear')
    print(line)

for line in lines:
    render(line)
    time.sleep(0.1)

render(lines[0])
