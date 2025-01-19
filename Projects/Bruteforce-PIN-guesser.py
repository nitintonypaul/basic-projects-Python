#4 digit numerical ping guesser program by Nitin Tony Paul
'''This is program is the demonstration of the concept of brute-force algorithm where a series of possible outcomes are tried until the correct
solution is obtained. This method is usually inefficient, but can be useful in certain situations like this one, where you're given to crack a 
4 digit numerical password'''

#Intro message
print('''
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄                                                     
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌                                                    
▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌                                                    
▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌                                                    
▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌                                                    
▐░░░░░░░░░░░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌                                                    
▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     ▐░▌   ▐░▌ ▐░▌                                                    
▐░▌               ▐░▌     ▐░▌    ▐░▌▐░▌                                                    
▐░▌           ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌                                                    
▐░▌          ▐░░░░░░░░░░░▌▐░▌      ▐░░▌                                                    
 ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀                                                     
                                                                                           
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌          ▐░▌       ▐░▌
▐░▌ ▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░▌▐░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌ ▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌                    ▐░▌          ▐░▌▐░▌          ▐░▌     ▐░▌  
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ ''')

#Decoration
print("---------------------------------------------------------------------------------------------")

#Asking the user for the secret pin to later find using bruteforce algorithm
secret_pin = input("Enter the secret 4-digit numerical pin: ")

#Some more decoration
print("---------------------------------------------------------------------------------------------")

#Starting a loop from 0 to 10,000 to include all the possible pin combinations
for i in range(10000):

    #Converting the number into pin format, i.e (1 --> 0001)
    guess = "0"*(4-len(str(i)))+str(i)

    #Printing the guess as a proof that I'm actually brute-forcing it. Otherwise how would you know, huh?
    print(guess)

    #checking if the guess matches with the secret pin
    if guess == secret_pin:

        #Displaying the guess
        print(f"BINGO! The secret pin found by brute-force algorithm is {guess}")

        #Breaking if the guess matches
        break
     
#Final set of decor
print("---------------------------------------------------------------------------------------------")
