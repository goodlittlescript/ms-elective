import signal
import time


def my_function():
    while True:
        print(f"the time is: {time.time()}")
        time.sleep(1)


def timeout_handler(signum, frame):
    raise TimeoutError("Function timed out!")


signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(5)  # Set timeout to 5 seconds

try:
    my_function()
except TimeoutError:
    pass
