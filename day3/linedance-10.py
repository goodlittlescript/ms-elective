import os

lines = [
    ".X.......",
    "..X......",
    "...X.....",
    "....X....",
    ".....X...",
    "......X..",
    ".......X.",
]

location = 5
print(lines[location])

cmd = input("enter move: ")
if cmd == "left":
    location -= 1
if cmd == "right":
    location += 1
print(lines[location])

cmd = input("enter move: ")
if cmd == "left":
    location -= 1
if cmd == "right":
    location += 1
print(lines[location])

cmd = input("enter move: ")
if cmd == "left":
    location -= 1
if cmd == "right":
    location += 1
print(lines[location])
