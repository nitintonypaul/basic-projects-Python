#Tic tac toe game by Nitin Tony Paul
'''The classic XOX game where two people play against each other by taking turns and strategically
planting their moves (X or O) in the given nine boxes. The first to get 3 of their characters in a
row either diagonally, horizontally or vertically wins the game.'''

'''Note: this is a simple version of the tic tac toe game and it may lack certain features and may contain certain glitches. The project's purpose is to teach basic python
and so I have decided to exclude certain features'''
#Modules used: none 


#Raw game board (backend version)
row1 = ["-","-","-"]
row2 = ["-","-","-"]
row3 = ["-","-","-"]

#Defining the function to check the status of the game
def checkWin():
    
    #Horizontal case
    if ((row1[0] == row1[1]) and (row1[1] == row1[2]) and (row1[0]!="-")) or ((row2[0] == row2[1]) and (row2[1] == row2[2]) and (row2[2]!="-")) or ((row3[0] == row3[1]) and (row3[1] == row3[2]) and (row3[0]!="-")):
        return False
    
    #Vertical case
    elif ((row3[0] == row2[0]) and (row2[0] == row1[0]) and (row3[0]!="-")) or ((row3[1] == row2[1]) and (row2[1] == row1[1]) and (row3[1]!="-")) or ((row3[2] == row2[2]) and (row2[2] == row1[2]) and (row3[2]!="-")):
        return False
    
    #Diagonal case
    elif ((row1[0] == row2[1]) and (row2[1] == row3[2]) and (row3[2]!="-")) or ((row1[2] == row2[1]) and (row2[1] == row3[0]) and (row3[0]!="-")):
        return False
    
    #If the above cases don't satisfy, we proceed to check for draw 
    else:
        #A very very inefficient, but easy method to check if the status of the game is draw
        counter = 0 #Initialising a variable as 0

        #iterating through each of the lists (row1, row2 and row3) and incrementing the counter variable by 1 if the element appears to be anything other than "-"
        #This way, if the counter variable is 9, it means that every single slot is filled but since there isn't a win, the game is a draw
        for i in row1:
            if i!="-":
                counter+=1
        for i in row2:
            if i!="-":
                counter+=1
        for i in row3:
            if i!="-":
                counter+=1

        #Exiting the game from within the function if the game appears to be a draw.... well along with an exit message
        if counter == 9:
            print("--------------------------------------------------------------------------------------------------")
            print("The game is a draw!")
            print("--------------------------------------------------------------------------------------------------")
            exit()
        else:
            return True


#Function to register a move to the game board
def registerMove(row,col,char):
    if row == 1:
        row1[col] = char
    elif row == 2:
        row2[col] = char
    elif row == 3:
        row3[col] = char

#Decoration + Intro text
print("--------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------")
print('''
 ________  __                  ________                          ________                    __ 
|        \|  \                |        \                        |        \                  |  \\
 \$$$$$$$$ \$$  _______        \$$$$$$$$______    _______        \$$$$$$$$______    ______  | $$
   | $$   |  \ /       \         | $$  |      \  /       \         | $$  /      \  /      \ | $$
   | $$   | $$|  $$$$$$$         | $$   \$$$$$$\|  $$$$$$$         | $$ |  $$$$$$\|  $$$$$$\| $$
   | $$   | $$| $$               | $$  /      $$| $$               | $$ | $$  | $$| $$    $$ \$$
   | $$   | $$| $$_____          | $$ |  $$$$$$$| $$_____          | $$ | $$__/ $$| $$$$$$$$ __ 
   | $$   | $$ \$$     \         | $$  \$$    $$ \$$     \         | $$  \$$    $$ \$$     \|  \\
    \$$    \$$  \$$$$$$$          \$$   \$$$$$$$  \$$$$$$$          \$$   \$$$$$$   \$$$$$$$ \$$
''')
print("--------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------")


#Decoration + starting message + displaying the game board
print("--------------------------------------------------------------------------------------------------")
print("The game starts!")
print(f'''                     |     |     
                  {row1[0]}  |  {row1[1]}  |  {row1[2]}  
                _____|_____|_____
                     |     |     
                  {row2[0]}  |  {row2[1]}  |  {row2[2]}  
                _____|_____|_____
                     |     |     
                  {row3[0]}  |  {row3[1]}  |  {row3[2]}  
                     |     |  ''') #It looks a bit deformed, but when you print it out it looks pretty... trust me!

#Initialising decider variable which decides the turn
decider = False;

#Starting a loop to initialise game
while checkWin():

    #Decoration, a lot of them
    print("--------------------------------------------------------------------------------------------------")

    #Deciding the turn
    if not decider:
        turn = "X"
    else:
        turn = "O"
    
    print(f"It's {turn}'s turn") #Displaying the turn

    #Asking for user inputs for row and column value
    row = int(input("Enter your row of choice > "))
    column = int(input("Enter your column of choice > "))
    column = column-1 #-1 is converting them into index (as index starts from 0)

    #Calling the function to register the move
    registerMove(row,column,turn)

    #Swapping the decider booooooooooolean
    if decider:
        decider = False
    else:
        decider = True
    
    #A lot of decoration
    print("--------------------------------------------------------------------------------------------------")
    #Displaying gameboard
    print(f'''                     |     |     
                  {row1[0]}  |  {row1[1]}  |  {row1[2]}  
                _____|_____|_____
                     |     |     
                  {row2[0]}  |  {row2[1]}  |  {row2[2]}  
                _____|_____|_____
                     |     |     
                  {row3[0]}  |  {row3[1]}  |  {row3[2]}  
                     |     |  ''')

#Final messages and dacerations
print("--------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------")
print("We have a winner! Congratulations!!")
print("--------------------------------------------------------------------------------------------------")






#I spelled decorations wrong in the previous comment