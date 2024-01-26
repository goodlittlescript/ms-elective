import os

# Wraps the location if it leaves the specified range.
#
# Note the range is [lower,upper) meaning it includes the
# lower value but only goes "up to" the upper value.
def wrap_location(location, lower, upper):
    if location >= upper:
        return lower
    elif location < lower:
        return upper - 1
    else:
        return location

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
location = wrap_location(location, 0, len(lines))
print(lines[location])

cmd = input("enter move: ")
if cmd == "left":
    location -= 1
if cmd == "right":
    location += 1
location = wrap_location(location, 0, len(lines))
print(lines[location])

cmd = input("enter move: ")
if cmd == "left":
    location -= 1
if cmd == "right":
    location += 1
location = wrap_location(location, 0, len(lines))
print(lines[location])
