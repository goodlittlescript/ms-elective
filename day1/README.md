# Day 1 - quiz game

Goals

- Run python
- Interact with your program
- Strings (str) and integers (int)
- Challenge: lists

## quiz-1

`#`
  Everything on a line after `#` is a comment. You use them to put notes in your code. Python ignores them but we as people find them useful.

`print()`
  Writes a string to your terminal.

**string**
  What programmers call text. Enclose some characters in "" to make one. Characters include letters, digits, punctuation, and whitespace. You can concatenate strings by using the `+` operation.

`input()`
  A function that reads one line of input from your terminal. Lines end with a newline, which is what the Enter key represents. In other words you hit Enter to make a line.

Functions "do stuff" in programs. Both print and input are examples. To call a function (aka make it "do stuff") you use parenthesis after the name of the function. Any strings/other objects in the parenthesis are called arguments.

```python
input()                 # call the "input" function
print("hello world")    # call the "print" function with one argument "hello world"
```

## quiz-2

`=` 
  Use the equals sign to assign a value to a variable. We use variables to hold values. Variables are usually one word like `response`.

`==`
  Use two equals sign to check if a two values are the same.

`if/else`
  Use these to control the flow of your program. There are some key syntax details like indentation and use of `:` to separate the condition (ex `response == "Y"`) from the next statement.

This code is simple, but has lots of things that might trip you up. Make sure your indentation is present and uniform (two spaces).

## quiz-3

`+`
  An operation to add together integers. Note we've already used `+` with strings to mean concatenation. With integers `+` is addition.

## quiz-4

`+`
  Notably _you can't add strings and integers_. Hence the last line of the program causes an error like `TypeError: can only concatenate str (not "int") to str`.

The real lesson here is that if you get an error message read it and it will usually give a strong hint as to what is wrong.

## quiz-5

`str()`
  A function to cast things like integers into strings.

To fix the error above we "cast" the integer into a string. Then we have two strings and so we can concatenate them.

## quiz-6

`questions = ["a","b","c"]`
  List creation

`for (question, answer) in questions:`
  Iteration of a list

This is really just a preview of how you can avoid repeating yourself for every single question. This might sorta intuitively make sense or it may make no sense at all. There's actually lists-within-a-list. You can see there is deeper indentation as well. It's well beyond day0. I'm showing it simply so you can see it.
