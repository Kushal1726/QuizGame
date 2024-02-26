print("welcome to my our Quiz!")

playing = input("You Should Play This Game!!! \n")

if playing.lower() != "yes":
    quit()

print("Okay! Your choice is Good :)")
score = 0

answer = input("ALU Stand for? \n")
if answer.lower() == "arithmetic logic unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("GPU Stand for? \n")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("RAM Stand for? \n")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What is the currency of India? \n")
if answer.lower() == "rupee":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("Who founded the search engine of Google? \n")
if answer.lower() == "larry page":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score)+ "questions correct!")
print("You got " + str((score / 5)* 100) + "%.")