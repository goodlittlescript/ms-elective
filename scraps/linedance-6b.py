import os
import time

lines = [
    # Make the character change when going forward/backward
    # forward  ">"
    # backward "<"
    ":>......:",
    ":.>.....:",
    ":..>....:",
    ":...>...:",
    ":....>..:",
    ":.....>.:",
    ":......<:",
    ":.....<.:",
    ":....<..:",
    ":...<...:",
    ":..<....:",
    ":.<.....:",
]

for _ in range(0, 3):
    for line in lines:
        os.system("clear")
        print(line)
        time.sleep(0.1)

render(line)
