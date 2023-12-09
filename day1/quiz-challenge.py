# Quiz Game
print("What is your name?")
name = input()

print("Hi " + name + ", lets play a game!")

questions = [
    ["What state are you in?", "Colorado"],
    ["What school are you in?", "Littleton Academy"],
]

for item in questions:
    question = item[0]
    answer = item[1]
    print(question)
    response = input()
    if response == answer:
        print("You win!")
    else:
        print("Sorry no, the answer is: " + answer)

