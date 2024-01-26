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

def wrap_location(location, lines):
    if location >= len(lines):
        return 0
    elif location < 0:
        return len(lines) - 1
    else:
        return location

location = 5
print(lines[location])

cmd = input("enter move: ")
if cmd == "left":
    location -= 1
if cmd == "right":
    location += 1
location = wrap_location(location, lines)
print(lines[location])

cmd = input("enter move: ")
if cmd == "left":
    location -= 1
if cmd == "right":
    location += 1
location = wrap_location(location, lines)
print(lines[location])

cmd = input("enter move: ")
if cmd == "left":
    location -= 1
if cmd == "right":
    location += 1
location = wrap_location(location, lines)
print(lines[location])
