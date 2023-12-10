import os
import time
import sys, termios, tty

def getch():
    fd = sys.stdin.fileno()
    orig = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)  # or tty.setraw(fd) if you prefer raw mode's behavior.
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, orig)
    
def render(line, location):
    os.system('clear')
    print("Actions: h (right) l (left) q (quit)")
    for index, char in enumerate(line):
        if index == location:
            sys.stdout.write("X")
        else:
            sys.stdout.write(char)
    sys.stdout.write("\n")

line = [
    ":",".",".",".",".",".",".",".",":"
]

location = 1
render(line, location)

while True:
    user_input = getch()

    new_location = location
    if user_input == "l":
        new_location += 1
    if user_input == "h":
        new_location -= 1
    if user_input == "q":
        print("Thanks for playing!")
        exit()

    if line[new_location] == ".":
        location = new_location

    render(line, location)
