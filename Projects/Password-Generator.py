#Password generator program by Nitin Tony Paul
'''A simple but useful password generator program which we can use to build complex passwords for important websites.
The program asks user for the number of characters and generates a password with uppercase, lowercase, numbers and special characters'''
#Modules used: random

#Importing the necessary module(s)
import random

#Assigning different lists for different sets of characters to chose separately
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
special = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';','<','>',',','.','/','?','\\','|']

#Intro message + Decoration
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print('''
.#####....####....####....####...##...##...####...#####...#####............####...######..##..##..######..#####....####...######...####...#####..
.##..##..##..##..##......##......##...##..##..##..##..##..##..##..........##......##......###.##..##......##..##..##..##....##....##..##..##..##.
.#####...######...####....####...##.#.##..##..##..#####...##..##..........##.###..####....##.###..####....#####...######....##....##..##..#####..
.##......##..##......##......##..#######..##..##..##..##..##..##..........##..##..##......##..##..##......##..##..##..##....##....##..##..##..##.
.##......##..##...####....####....##.##....####...##..##..#####............####...######..##..##..######..##..##..##..##....##.....####...##..##.
.................................................................................................................................................
''')
print("----------------------------------------------------------------------------------------------------------------------------------------------")

#Asking the user for the number of characters
charNumbers = int(input("Enter number of characters required (minimum 4) > "))

#Checking if the specified input is lesser than 4, if so using a while loop to keep on asking the user until a valid response is given
while charNumbers < 4:
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("The minimum number of characters required must be 4! Try again!")
    charNumbers = int(input("Enter number of characters required (minimum 4) > "))

#Lots and lots of decoration
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------------------------------")

#initializing the empty password string 
password = ""

#Deducting 4 numbers off the userinput for the minimum requirements
charNumbers = charNumbers-4

password += uppercase[random.randint(0,len(uppercase)-1)] #Random uppercase character
password += lowercase[random.randint(0,len(lowercase)-1)] #Random lowercase character
password += special[random.randint(0,len(special)-1)] #Random special character
password += numbers[random.randint(0,len(numbers)-1)] #Random number

#Adding the lists and forming a parent list to pick out numbers, letters or special characters at complete random
good_list = uppercase + lowercase + special + numbers

#Conducting a loop through charNumbers
for i in range(charNumbers):
    password += good_list[random.randint(0,len(good_list)-1)] #Each time we pick a random character from good_list and add into the password string

#One last shuffle of the string to make it a little bit more random
password = list(password) #Converting into list
random.shuffle(password) #Shuffling list
password = "".join(password) #Re-Converting into string

#Displaying the random password
print(f"A random password generated is '{password}'")

#Final set of decoration
print("----------------------------------------------------------------------------------------------------------------------------------------------")