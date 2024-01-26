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

def bound_location(location, lines):
    if location >= len(lines):
        return len(lines) - 1
    elif location < 0:
        return 0
    else:
        return location

location = 5
print(lines[location])

cmd = input("enter move: ")
if cmd == "left":
    location -= 1
if cmd == "right":
    location += 1
location = bound_location(location, lines)
print(lines[location])

cmd = input("enter move: ")
if cmd == "left":
    location -= 1
if cmd == "right":
    location += 1
location = bound_location(location, lines)
print(lines[location])

cmd = input("enter move: ")
if cmd == "left":
    location -= 1
if cmd == "right":
    location += 1
location = bound_location(location, lines)
print(lines[location])
