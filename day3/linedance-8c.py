import os

line = [
  ".",
  ".",
  ".",
  ".",
  ".",
  ".",
  ".",
  ".",
  "."
]

def render(line, location):
    os.system("clear")
    for index, char in enumerate(line):
        if index == location:
            print("X")
        else:
            print(char)

render(line, 1)
print("location 1")
input()

render(line, 2)
print("location 2")
input()

render(line, 3)
print("location 3")
input()

render(line, 4)
print("location 4")
input()

render(line, 5)
print("location 5")
input()

render(line, 6)
print("location 6")
input()

render(line, 7)
print("location 7")
input()
