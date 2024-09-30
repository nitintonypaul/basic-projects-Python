#Number guessing game by Nitin Tony Paul
'''A random number will be selected from 1 to n where n is inputed by the user.
The user has to try to guess the number with minimum tries'''
#Modules used: random

#Importing necessary module(s)
import random #Built-in module

#Decoration + intro text + decoration
print("---------------------------------------------------------------------------------")
print('''
,-,-.             .                                                                /\ 
` | |   . . ,-,-. |-. ,-. ,-.   ,-. . . ,-. ,-. ,-. . ,-. ,-.    ,-. ,-. ,-,-. ,-. )( 
  | |-. | | | | | | | |-' |     | | | | |-' `-. `-. | | | | |    | | ,-| | | | |-' \/ 
 ,' `-' `-^ ' ' ' ^-' `-' '     `-| `-^ `-' `-' `-' ' ' ' `-|    `-| `-^ ' ' ' `-' :; 
                                 ,|                        ,|     ,|                  
                                 `'                        `'     `'                  
''')
print("---------------------------------------------------------------------------------")

#Asking input from the user for the range of the game
n = int(input("Enter range of the numbers (Note: Increasing your range will increase difficulty) > "))

#Selecting a random integer within the range and starting the game (with a touch of decoration)
randomNumber = random.randint(1,n)
print("The game starts now!")
print("---------------------------------------------------------------------------------")

#Initialising the 'tries' variable
tries = 1

#Obtaining the first guess
guess = int(input(f"Enter guess #{tries} > "))

#Running a while loop for further guesses
while guess!=randomNumber: #Checking if the guess is equal to the random number

    #Hint cases
    #Dispaly if the guess is lesser or greater than the random number
    if guess > randomNumber:
        print("Wrong guess! The mystery number is lesser than your guess!")
    else:
        print("Wrong guess! The mystery number is greater than your guess")
    
    print("---------------------------------------------------------------------------------") #More decoration

    #Incrementing Tries to keep track
    tries +=1

    #Reassigning the guess variable by obtaining user input
    guess = int(input(f"Enter guess #{tries} > "))

#If the player cracked the mystery number
print("---------------------------------------------------------------------------------") #Even more decoration
print(f"Good job! You cracked the Number guessing game in {tries} tries!") #Congratulating the player and displaying the number of tries
print("---------------------------------------------------------------------------------") #Final decoration
