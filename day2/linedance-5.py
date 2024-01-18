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

# returns the current time in seconds
start = time.time()

for line in lines:
    os.system("clear")
    print(line)
    time.sleep(0.1)

# so we can calculate the elapsed time
finish = time.time()
elapsed = finish - start

print("You won in: " + str(elapsed) + "s")
