#Grocery receipt and price calculator program by Nitin Tony Paul
'''This program is a useful too to list down the groceries required and to calculate the price required before going to the store. It uses a nested
list to store the item details which is later then extracted and used to calculate the display the receipt to the user'''

#Intro message
print('''
       __         ___        ___        ___              __    ___  ___   ___                                         
  .'|=|  |   .'|=|_.'   .'|=|_.'   .'|=|_.'   .'|   .'|=|  |  `._|=|   |=|_.'                                         
.'  | |  | .'  |  ___ .'  |      .'  |  ___ .'  | .'  | |  |       |   |                                              
|   |=|.'  |   |=|_.' |   |      |   |=|_.' |   | |   |=|.'        |   |                                              
|   |  |`. |   |  ___ `.  |  ___ |   |  ___ |   | |   |            `.  |                                              
|___|  |_| |___|=|_.'   `.|=|_.' |___|=|_.' |___| |___|              `.|                                              
                                                                                                                      
                   ___                        __          __               ___        ___                             
  .'|=|`.     .'| |   |   .'|=|`.        .'|=|  |    .'|=|  |   .'|   .'|=|_.'   .'|=|_.'                             
.'  | |  `. .'  |\|   | .'  | |  `.    .'  | |  |  .'  | |  | .'  | .'  |      .'  |  ___                             
|   |=|   | |   | |   | |   | |   |    |   |=|.'   |   |=|.'  |   | |   |      |   |=|_.'                             
|   | |   | |   | |  .' |   | |  .'    |   |       |   |  |`. |   | `.  |  ___ |   |  ___                             
|___| |___| |___| |.'   |___|=|.'      |___|       |___|  |_| |___|   `.|=|_.' |___|=|_.'                             
                                                                                                                      
       ___                               ___  ___                                ___  ___   ___                    __ 
  .'|=|_.'   .'|=|`.     .'|        .'|=|_.' |   | |`.     .'|        .'|=|`.   `._|=|   |=|_.'   .'|=|`.     .'|=|  |
.'  |      .'  | |  `. .'  |      .'  |      |   | |  `. .'  |      .'  | |  `.      |   |      .'  | |  `. .'  | |  |
|   |      |   |=|   | |   |      |   |      |   | |   | |   |      |   |=|   |      |   |      |   | |   | |   |=|.' 
`.  |  ___ |   | |   | |   |  ___ `.  |  ___ `.  | |   | |   |  ___ |   | |   |      `.  |      `.  | |  .' |   |  |`.
  `.|=|_.' |___| |___| |___|=|_.'   `.|=|_.'   `.|=|___| |___|=|_.' |___| |___|        `.|        `.|=|.'   |___|  |_|''')

#Decoration
print("-----------------------------------------------------------------------------------------------------------------------")

#Item list, this is a nested list to store item details
item_list = []

#An infinite loop so that the user decides when to stop
while True:

    #Obtaining the item/exit using EXIT command
    item = input("Enter the name of the item (type EXIT to exit the program): ")
    
    #Exiting the input process if specified
    if item.lower() == 'exit':
        break

    #Obtaining the quantity and the price of the item
    quantity = int(input("Enter the quantity of the item: "))
    price = float(input("Enter the price: "))

    #Adding the item details into the item list
    item_list.append([item, price, quantity])

    #Decoration to separate item
    print("-----------------------------------------------------------------------------------------------------------------------")


#Declaring the total variable to store sum of all prices
total = 0

#White spaces for better aesthetic
print(" ")

#Receipt decoration
print("-----------------------------")

#Heading
print("RECEIPT")

#Receipt decoration
print("-----------------------------")

#Extracting each item and displaying them with their price and their quantity
for i in item_list:
    print(f" {i[0]} - ${i[1]}    {i[2]}nos. ")

    #Adding the price into the total variable
    total += price*quantity

#Displaying total price in the end
print(f"TOTAL    :   ${total}")

#Wrap up decoration
print("-----------------------------------------------------------------------------------------------------------------------")