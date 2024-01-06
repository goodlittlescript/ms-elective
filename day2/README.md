# Day 2 - linedance game

Goals

- Animate output
- Learn `import`, `os.system("clear")`, and `time.sleep()`
- Make a button smasher

## linedance-1

Hit enter to kinda-sorta see motion.

## linedance-2

`import`
  Python is pretty big. Not everything is available by default, because it would take too long to load. Use `import` to bring in _modules_ of things that your program happens to need.

`import os`
  Imports the [operating system module](https://docs.python.org/3/library/os.html) to interact with your operating system (in this case our terminal) 

`os.system("clear")`
  Clears the terminal

Clear the terminal after each input and now we have motion! This is how screens work. They're constantly clearing and redrawing themselves. We precieve the result as motion even though it's really a series of snapshots.

## linedance-3

`lines = [...]`
  Make a list of lines

`for line in lines:`
  Iterate the list

This lets us not repeat ourselves for each line.

## linedance-4

`import time`
  Imports the [time module](https://docs.python.org/3/library/time.html) to get access to a clock.

`time.time()`
  Gets the current time

`elapsed = finish - start`
  Calculate the elapsed time. Note we're using math on variables.

Now we've got a button smasher! How fast can you win?

## linedance-5

`time.sleep(N)`
  Sleep (aka "pause") for N seconds.

Using sleep instead of waiting for input allows us to have the motion occur by itself.

## linedance-6 (challenge)

`while iteration < 3:`
  Loop while the condition `iteration < 3` evaluates to `True`. 

This is a challenge that shows how you can loop over a loop multiple times.
