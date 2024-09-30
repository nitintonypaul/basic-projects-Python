#Rock Paper Scissors game by Nitin Tony Paul
'''A game where the user inputs a number which is the number of rounds in the game. In each round
the user can select and option from rock, paper or scissors. The computer will make a random decision and
soon the final results will be drawn based on Rock < Paper < Scissors < Rock ('<' meaning beats)'''
#Modules used: random

#Defining the function to check the status of the round (win, lose or draw)
def checkWin(user, comp):

    #Win case
    if (user == 'r' and comp=='s') or (user == 's' and comp=='p') or (user == 'p' and comp=='r'):
        return 1
    
    #Draw case
    elif user==comp:
        return 0
    
    #Final case (lose case)
    else:
        return -1

#Importing necessary module(s)
import random

#Decorative Intro text
print("---------------------------------------------------------------------------------")
print('''
___________________________________________________________________________________________________________________________
    ____                           ____                                     __                                           / 
    /    )               /         /    )                                 /    )         ,                              /  
---/___ /----__----__---/-__------/____/----__------__----__---)__--------\--------__-------__---__----__---)__---__---/---
  /    |   /   ) /   ' /(        /        /   )   /   ) /___) /   )        \     /   ' /   (_ ` (_ ` /   ) /   ) (_ ` /    
_/_____|__(___/_(___ _/___\_____/________(___(___/___/_(___ _/_________(____/___(___ _/___(__)_(__)_(___/_/_____(__)_o_____
                                                /                                                                          
                                               /                                                                           
''')
print("---------------------------------------------------------------------------------")

#Asking the user input for number of rounds aka roundCount-
roundCount = int(input("Enter the number of rounds (must be an odd number) > "))

#Checking if the number of rounds are even, if so asking them to input again
while not (roundCount%2):
    print("That is not an odd number, please enter again!")
    print("---------------------------------------------------------------------------------")
    roundCount = int(input("Enter the number of rounds (must be an odd number) > "))

#More decoration and notifying the start of the game
print("---------------------------------------------------------------------------------")
print("The game starts now!")
print("---------------------------------------------------------------------------------")

#Defining a list for the set of choices both the user and the computer have
choiceList = ['r','p','s']

#Defining user's and computer's score (currently set to 0)
userScore,computerScore = 0,0

#Starting a for loop for roundCount number of times
#Small modification as I incremented the start and stop values to display the round number easier
for i in range(1,roundCount+1):
    print(f"Round number {i}") #Displaying the round number

    #Asking for user input in the ith round
    userChoice = input("Enter your choice (r,p or s) > ").lower()

    #Checking if the user's choice is invalid, if so asking them to input again
    while userChoice not in choiceList:
        print("That is not a valid option! Please try again.")
        userChoice = input("Enter your choice (r,p or s) > ").lower()
    
    #Using random, the computer makes it's own choice
    #Here I select an integer randomly from 0-2 and set that as a list index for choiceList, which becomes the computer's choice
    computerChoice = choiceList[random.randint(0,2)]

    #Decorative texts
    print("---------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------")

    #Displaying both user's and computer's choices
    print(f"User choice: {userChoice}")
    print(f"Computer choice: {computerChoice}")

    #Sending both choices in the checkWin function which returns a value depending upon the status of the round
    #The value is stored in winChecker
    winChecker = checkWin(userChoice,computerChoice)

    #Checking the value of winChecker

    #Lose case
    if winChecker<0:
        print("The computer won this round!")
        computerScore +=1 #Incrementing computer's score
    
    #Draw case
    elif not winChecker:
        print("This round is a draw!")
                                        #Not incrementing anyone's score
    
    #Win case
    else:
        print("The user won this round!")
        userScore +=1 #Incrementing user's score

    #That's a lot of decorative text
    print("---------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------")

#Displaying both user's and computer's final score
print(f"User scored {userScore} points")
print(f"Computer scored {computerScore} points")

#I can't stop typing these decorations!
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")

#Checking both user's and computer's final score to print the final message

#Win case
if userScore > computerScore:
    print("Congratulations on winning the game!!")

#Draw case
elif userScore == computerScore:
    print("It's a draw!! Good game!!")

#Lose case
else:
    print("The computer won the game!! Better luck next time!")

#Finally, the game ends with one last piece of cake- I mean decoration
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")


#Wow I'm so tired.