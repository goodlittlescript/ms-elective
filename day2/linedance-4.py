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
    ".X.......",
]

for line in lines:
    os.system('clear')
    print(line)
    time.sleep(0.1)
