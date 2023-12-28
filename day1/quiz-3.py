# Quiz Game
score = 0

print("What is your name?")
name = input()

print("Hi " + name + ", lets play a game!")

print("What state are you in?")
response = input()
if response == "Colorado":
    print("You win!")
    score += 1
else:
    print("Sorry no, the answer is: Colorado")

print("What school are you in?")
response = input()
if response == "Littleton Academy":
    print("You win!")
    score += 1
else:
    print("Sorry no, the answer is: Littleton Academy")

print("Your score is: " + str(score))
