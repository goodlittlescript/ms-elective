# Quiz Game + math (broken)
print("Lets play a game!")
score = 0

print("What is 34 + 8")
answer = 34 + 8
response = input()
if response == answer:
    print("You win!")
    score = score + 1
else:
    print("Sorry the correct answer is: " + str(answer))

print("What is 52 - 10")
answer = 52 - 10
response = input()
if response == answer:
    print("You win!")
    score = score + 1
else:
    print("Sorry the correct answer is: " + str(answer))

print("What is 6 * 7")
answer = 6 * 7
response = input()
if response == answer:
    print("You win!")
    score = score + 1
else:
    print("Sorry the correct answer is: " + str(answer))

print("What is 84 / 2")
answer = 84 / 2
response = input()
if response == answer:
    print("You win!")
    score = score + 1
else:
    print("Sorry the correct answer is: " + str(answer))

print("Your score is: " + str(score))
