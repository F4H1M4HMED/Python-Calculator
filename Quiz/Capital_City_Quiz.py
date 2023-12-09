print("Welcome to the Capital City Quiz Game!")
playing = input("Do you want to play? (yes/no): ").lower()
if playing != "yes":
    print("Bye!")
    quit()

print("OK! Let's Play!")
score = 0

answer = input("What is the capital city of Spain? ")
if answer.lower() == "madrid":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital city of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital city of Germany? ")
if answer.lower() == "berlin":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital city of Italy? ")
if answer.lower() == "rome":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital city of The Netherlands? ")
if answer.lower() == "amsterdam":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("End of Quiz")
print(f"You got {score} questions correct")
print(f"Your score is {score/5 * 100}%")
print("Goodbye!")




