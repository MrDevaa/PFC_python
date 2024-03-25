print("Bienvenue dans mon quiz !")

playing = input("Voulez-vous jouer au Quiz ?")

if playing.lower() != "yes":
    quit()

print("Super! jouons :) ")
score = 0

answer = input("What does CPU stand for ?")

if answer.lower() == "central processing unit":
    print('Correct !')
    score += 1
else:
    print('Incorrect :(')

answer = input("What does GPU stand for ?")

if answer.lower() == "G processing unit":
    print('Correct !')
    score += 1

else:
    print('Incorrect :(')

answer = input("What does CPU stand for ?")

if answer.lower() == "central processing unit":
    print('Correct !')
    score += 1
else:
    print('Incorrect :(')

answer = input("What does CPU stand for ?")

if answer.lower() == "central processing unit":
    print('Correct !')
    score += 1
else:
    print('Incorrect :(')


print("you got" + str(score) + "question correct")
print("you got" + str((score/4) * 100) + "%")