# Quiz Game + score
print("Lets play a game!")
score = 0

print("Is water wet? (enter Y or N)")
response = input()
if response == "Y":
    print("You win!")
    score = score + 1
else:
    print("Sorry the correct answer is: Y")

print("Is an apple an orange? (enter Y or N)")
response = input()
if response == "N":
    print("You win!")
    score = score + 1
else:
    print("Sorry the correct answer is: N")

print("Your score is: " + str(score))
