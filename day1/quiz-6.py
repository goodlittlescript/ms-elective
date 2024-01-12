# Quiz Game + lists
print("Lets play a game!")
score = 0

questions = [
    ["Is water wet?", "Y"],
    ["Is an apple an orange?", "N"],
]

for (question, answer) in questions:
    print(question + " (enter Y or N)")
    response = input()
    if response == answer:
        print("You win!")
        score += 1
    else:
        print("Sorry no, the answer is: " + answer)

print("Your score is: " + str(score))
