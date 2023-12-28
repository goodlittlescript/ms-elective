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
    # Removed the last one...
]

for _ in range(0, 3):
    for line in lines:
        os.system("clear")
        print(line)
        time.sleep(0.1)

os.system("clear")
print(lines[0])
