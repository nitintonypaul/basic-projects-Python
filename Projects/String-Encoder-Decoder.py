#BMI string encoder/decoder program by Nitin Tony Paul
'''A simple string decoder and encoder program to encode or decode a string using the XOR method of encryption. Decoded strings are not readable by humans and hence can
be stored well without others sniping in your little secrets'''

#Intro message
print('''
.oOOOo.                                                         
o     o               o                                         
O.         O                                                    
 `OOoo.   oOo                                                   
      `O   o   `OoOo. O  'OoOo. .oOoO                           
       o   O    o     o   o   O o   O                           
O.    .O   o    O     O   O   o O   o                           
 `oooO'    `oO  o     o'  o   O `OoOo                           
                                    O                           
                                 OoO'                           
o.OOoOoo                         o                     .oOOOo.  
 O                              O                      O     o  
 o                              o                       O  o'   
 ooOO                           o                        OO     
 O       'OoOo. .oOo  .oOo. .oOoO  .oOo. `OoOo.        o' o     
 o        o   O O     O   o o   O  OooO'  o           O    Oo o 
 O        O   o o     o   O O   o  O      O           `o     O' 
ooOooOoO  o   O `OoO' `OoO' `OoO'o `OoO'  o            `OoooO Oo
                                                                
                                                                
o.OOOo.                          o                              
 O    `o                        O                               
 o      O                       o                               
 O      o                       o                               
 o      O .oOo. .oOo  .oOo. .oOoO  .oOo. `OoOo.                 
 O      o OooO' O     O   o o   O  OooO'  o                     
 o    .O' O     o     o   O O   o  O      O                     
 OooOO'   `OoO' `OoO' `OoO' `OoO'o `OoO'  o                     ''')


#Decoration
print("----------------------------------------------------------------------------")

string = input("Enter the string to be encoded or decoded: ")

#More decoration
print("----------------------------------------------------------------------------")

#Key is selected here
key = 20

#Result string
res = ""

#For loop to find the message hidden or hide the message given
for i in string:

    #XOR method of encryption and adding the encrypted/decrypted character to the string
    res += chr(key^ord(i))

#Displaying the result
print(f"The decoded/encoded string is {res}")

#Final decoration
print("----------------------------------------------------------------------------")