import random
choic = ["P", "K", "N"]
def pkn():
    computer_choice = random.choice(choic)
    if computer_choice == "K":
        computer_choice_kamień()
    elif computer_choice == "P":
        computer_choice_papier()
    else:
        computer_choice_nożyce()
def computer_choice_kamień():
    user_choice = input("Wybierz figurę: K - kamień, P - papier, N - nożyce: ")
    if user_choice == "K":
        print("Kamien")
        print ("Remis!")
        try_again()
    if user_choice == "P":
        print("Kamien")
        print ("Gracz wygrywa!")
        try_again()
    if user_choice == "N":
        print("Kamien")
        print ("Komputer wygrywa!")
        try_again()
    else:
        print ("Spróbuj ponownie")
        computer_choice_kamień()

def computer_choice_papier():
    user_choice = input("Wybierz figurę: K - kamień, P - papier, N - nożyce: ")
    if user_choice == "K":
        print("Papier")
        print ("komputer wygrywa!")
        try_again()
    if user_choice == "P":
        print("Papier")
        print ("Remis!")
        try_again()
    if user_choice == "N":
        print("Papier")
        print ("Gracz wygrywa!")
        try_again()
    else:
        print ("Spróbuj ponownie")
        computer_choice_papier()

def computer_choice_nożyce():
    user_choice = input("Wybierz figurę: K - kamień, P - papier, N - nożyce: ")
    if user_choice == "K":
        print("Nożyce")
        print ("Gracz wygrywa!")
        try_again()
    if user_choice == "P":
        print("Nożyce")
        print ("Komputer wygrywa!")
        try_again()
    if user_choice == "N":
        print("Nożyce")
        print ("Remis!")
        try_again()
    else:
        print ("Spróbuj ponownie")
        computer_choice_nożyce()
def try_again():
    choice = input("Czy chcesz grać dalej?? [t/n] ")
    if choice == "t":
        pkn()
    elif choice == "n":
        
        quit()
    else:
        print ("Spróbuj ponownie")
        try_again()
pkn()
