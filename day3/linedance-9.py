import os

lines = [
    ":X......:",
    ":.X.....:",
    ":..X....:",
    ":...X...:",
    ":....X..:",
    ":.....X.:",
    ":......X:",
]

locations = [
    # loops
    0,1,2,3,4,5,6,
    0,1,2,3,4,5,6,
    0,1,2,3,4,5,6,

    # back and forth
    0,1,2,3,4,5,6,
    5,4,3,2,1,0,
    1,2,3,4,5,6,
    5,4,3,2,1,0,

    # jump around
    6,0,6,0,6,0,6,0,6,0
]

for location in locations:
    os.system("clear")
    print(lines[location])
    input()
