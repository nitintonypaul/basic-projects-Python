#Morse code translator by Nitin Tony Paul
'''In this program one will be able to translate morse code to english. Even though morse code is not used much around in the 21st century, it's a fun
program to learn various data types and logics in Python. Enjoy!'''
#Modules used: None

#Introduction and decoration
print("----------------------------------------------------------------------------------------------------------------------------------")
print('''
 _______                                 ______            __             __                               __         __                
|   |   |.-----..----..-----..-----.    |      |.-----..--|  |.-----.    |  |_ .----..---.-..-----..-----.|  |.---.-.|  |_ .-----..----.
|       ||  _  ||   _||__ --||  -__|    |   ---||  _  ||  _  ||  -__|    |   _||   _||  _  ||     ||__ --||  ||  _  ||   _||  _  ||   _|
|__|_|__||_____||__|  |_____||_____|    |______||_____||_____||_____|    |____||__|  |___._||__|__||_____||__||___._||____||_____||__|  
''')
print("----------------------------------------------------------------------------------------------------------------------------------")

#Creating morse dictionary which is.... a dictionary in Python
#dictionaries are an iterable data type with a key and a value, which is very useful for storing related information..just like this one
morse_data = {'.-':'A',
              '-...':'B',
              '-.-.':'C',
              '-..':'D',
              '.':'E',
              '..-.':'F',
              '--.':'G',
              '....':'H',
              '..':'I',
              '.---':'J',
              '-.-':'K',
              '.-..':'L',
              '--':'M',
              '-.':'N',
              '---':'O',
              '.--.':'P',
              '--.-':'Q',
              '.-.':'R',
              '...':'S',
              '-':'T',
              '..-':'U',
              '...-':'V',
              '.--':'W',
              '-..-':'X',
              '-.--':'Y',
              '--..':'Z',
              '.----':'1',
              '..---':'2',
              '...--':'3',
              '....-':'4',
              '.....':'5',
              '-....':'6',
              '--...':'7',
              '---..':'8',
              '----.':'9',
              '-----':'0',
              '/': ' '}

#Instructions for use
print("Instructions\n- Use . and - for characters\n- Use a space to separate between letters\n- Use a slash / and space on either side to separate between words")
print("----------------------------------------------------------------------------------------------------------------------------------")

#Asking the user for the input
morseString = input("Enter message in morse: ")

#More decoration
print("----------------------------------------------------------------------------------------------------------------------------------")

#Converting the string to a list by splitting it at spaces (' ') to separate letters
morseList = morseString.split(" ")

#Assigning an empty string to concatenate the result of each letter
resultSTR = ""

#Iterating through the list to extract each character and finding the equivalent english letter
for i in morseList:
    resultSTR += morse_data[i] #Using the key of the dictionary to extract the value and concatenate to the resultSTR

#Displaying the result string while capitalising for aesthetic
print(f"Translation: {resultSTR.capitalize()}")
print("----------------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------------------")


#Done!