import os


# Bounds the location if it leaves the specified range.
#
# Note the range is [lower,upper) meaning it includes the
# lower value but only goes "up to" the upper value.
def bound_location(location, lower, upper):
    if location >= upper:
        return upper - 1
    elif location < lower:
        return lower
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

keymap = {
    "h": "left",
    "l": "right",
    "q": "quit",
}

location = 5
print(lines[location])

while True:
    key = input("enter move: ")
    cmd = keymap.get(key, "unknown")

    if cmd == "left":
        location -= 1
    if cmd == "right":
        location += 1
    if cmd == "quit":
        break
    if cmd == "unknown":
        pass

    location = bound_location(location, 0, len(lines))
    print(lines[location])
