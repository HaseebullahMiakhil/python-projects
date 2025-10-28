import sys
import random

your_input = input("\n\n please enter a number: \n: stone\n2 : paper\n3 scissors\n\n")
if your_input.isdigit():
    your_chice = int(your_input)
    if (your_chice <0 or your_chice > 3):
        print("you must enter 1 or 2 or 3")
        sys.exit()
    
    computer_value = random.choice("123")
    computer_choice = int(computer_value)
    
    print("your choice is " + your_input + "\n computer choice is "+ computer_value)

    if your_chice == 1 and computer_value == 3:
        print("you win")
    elif your_chice == 2 and computer_value ==3:
        print("you win")
    elif your_chice == 3 and computer_choice == 2:
        print("you win!")
    elif your_chice == computer_choice:
        print("tie game")
    else :
        print("computer win")

else:
    print("you must enter a valid number.")
