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

iteration = 0
while iteration < 3:
    for line in lines:
        os.system("clear")
        print(line)
        time.sleep(0.1)
    iteration += 1
