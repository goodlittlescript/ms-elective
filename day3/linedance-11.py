import os
import time
import sys

line = [":", ".", ".", ".", ".", ".", ".", ".", ":"]
locations = [1,2,3,4,5,6,7,6,5,4,3,2]

def render(line, location):
    os.system("clear")
    for index, char in enumerate(line):
        if index == location:
            sys.stdout.write("X")
        else:
            sys.stdout.write(char)
    sys.stdout.write("\n")
   

for _ in range(0,3):
    for location in locations:
        render(line, location)
        time.sleep(0.1)
render(line, 1)
