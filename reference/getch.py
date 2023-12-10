import sys, termios, tty


def getch():
    fd = sys.stdin.fileno()
    orig = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)  # or tty.setraw(fd) if you prefer raw mode's behavior.
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, orig)
    
