import random

user_wins = 0
computer_wins = 0

options = ["pierre","feuille","ciseaux"]

while True:
    user_input = input("Type Pierre/Feuille/Ciseaux ou Q pour quitter: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2) 
    # pierre: 0, feuille: 1, ciseaux: 2
    computer_pick = options[random_number]
    print("Adversaire a choisi", computer_pick + ".")

    #first condition 
    if user_input == "pierre" and computer_pick == "ciseaux":
        print("tu as gagné !")
        user_wins += 1
        
    #second condition 
    elif user_input == "feuille" and computer_pick == "pierre":
        print("tu as gagné !")
        user_wins += 1
        
    #third condition 
    elif user_input == "ciseaux" and computer_pick == "feuille":
        print("tu as gagné !")
        user_wins += 1

    else: 
        print("tu as perdu :|")
        computer_wins += 1


#print pour users
print("Vous avez gagner", user_wins, "fois.")
#print pour adversaire
print("Votre adversaire a gagner", computer_wins, "fois.")
#fin
print("Aurevoir !")
