# SNAKE, WATER AND GUN GAME:-

'''
 1 for water,
-1 for Snake,
 0 for Gun.
'''

#importing random module for computer turns
import random

computer = random.choice([-1, 0, 1])
your_choice = input("Enter your choice: ")
your_dict = {"snake":-1, "water":1, "gun":0}
you = your_dict[your_choice]
reversed_dict = {-1:"snake", 1:"water", 0:"gun"}

#printing the choices made
print(f"You chose: {reversed_dict[you]}\nComputer chose: {reversed_dict[computer]}")

if(computer == you):
    print("It's a Draw!\n   Play Again..")

else:
    if(computer==1 and you==-1):
        print("Hurray! You Win! ")

    elif(computer==-1 and you==1):
        print("You lose! :(")
    
    elif(computer==0 and you==1):
        print("Hurray! You Win! ")

    elif(computer==1 and you==0):
        print("You lose! :(")

    elif(computer==0 and you==-1):
        print("You lose! :(")
    
    elif(computer==-1 and you==0):
        print("Hurray! You Win! ")

    else:
        print("Something went wrong..")

