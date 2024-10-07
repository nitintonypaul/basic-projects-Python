#BMI calculator by Nitin Tony Paul
'''A simple BMI calculator used to check if you're underweight, healthy or obese. Body Mass Index (BMI) is widely used to determine if a person is 
overweight or underweight.'''
#Modules used: None

#Intro message
print('''
 ______ _______ _______                  __              __         __              
|   __ \   |   |_     _|    .----.---.-.|  |.----.--.--.|  |.---.-.|  |_.-----.----.
|   __ <       |_|   |_     |  __|  _  ||  ||  __|  |  ||  ||  _  ||   _|  _  |   _|
|______/__|_|__|_______|    |____|___._||__||____|_____||__||___._||____|_____|__|  
                                                                                    
''')
#Added decoration
print("-------------------------------------------------------------------------------------------")
weight = float(input("Enter your weight in kg > ")) #Asking for weight in kilograms
height = float(input("Enter your height in cm > ")) #Asking for weight in cm

#Checking for negative values
while weight < 0 or height < 0:
    #Printing message
    print("One of the values you've inputed is invalid! Try again!")

    weight = float(input("Enter your weight in kg > ")) #Asking for weight in kilograms (again)
    height = float(input("Enter your height in cm > ")) #Asking for weight in cm (again)

#Decoration
print("-------------------------------------------------------------------------------------------")

#Calculating BMI
#BMI = weight in kilograms ÷ height in cm, squared
BMI = weight/((height/100)**2)

#Classifying their message regarding weight according to their BMI
if BMI <= 18.4:
    print(f"You are underweight with a BMI of {BMI}!")
elif BMI > 18.4 and BMI <= 24.9:
    print(f"You have a healthy weight with a BMI of {BMI}!")
elif BMI > 24.9 and BMI <= 39.9:
    print(f"You are overweight with a BMI of {BMI}!")
else:
    print(f"You are obese with a BMI of {BMI}!")

#Final decoration
print("-------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------")