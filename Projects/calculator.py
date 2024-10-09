#Calculator program by Nitin Tony Paul
'''This is a efficient calculator program which is used to evaluate complex expressions using +-/* and even % (modulo)
It's very easy to write and can be a very good debut project for many beginners.

NOTE: This program has a lot of drawbacks and cases which are not considered,yet since it is supposed to be used in a learning sense, I've currently ignored the complexes cases and shared the base code.'''

#Introduction + decoration
print('''
 ,-.     .         .     .             ;-.                            
/        |         |     |             |  )                           
|    ,-: | ,-. . . | ,-: |-  ,-. ;-.   |-'  ;-. ,-. ,-: ;-. ,-: ;-.-. 
\    | | | |   | | | | | |   | | |     |    |   | | | | |   | | | | | 
 `-' `-` ' `-' `-` ' `-` `-' `-' '     '    '   `-' `-| '   `-` ' ' ' 
                                                    `-'               
''')
print("-------------------------------------------------------------------------")

#Instructions for usage
print('''Instructions:\nuse (+) for plus\n(-) for minus\n(/) for division\n(*) for multiplication\n(%) for modulo [remainder]\n(**) for denoting power (x^y)\n\n Input your values with an expression. Example: 4*5-3+21\nType 'exit' to exit the program''')
#More decoration
print("-------------------------------------------------------------------------")

#Asking the user for the expression to evaluate
calculateString = input("Enter > ")

#Sending the expression through a while loop while checking if the inputed command is to exit
while calculateString.lower() != "exit": #the loop runs while the inputed command is not 'exit'
    
    #Using the eval function to quickly evaluate a string, assigning the value to a variable
    result = eval(calculateString)

    #Displaying the result
    print(result)
    
    #A decoration to separate the commands
    print("-------------------------------------------------------------------------")

    #Reassigning the calculateString variable
    calculateString = input("Enter > ")

#Exiting decoration + goodbye message
print("-------------------------------------------------------------------------")
print("Exiting the program...")
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")


#Very easy stuff :)