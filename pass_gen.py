import random
import string

def gen_pass(length,number=True,special_char=True):
    letters=string.ascii_letters # for alphabelts
    digits=string.digits # for numbers
    special=string.punctuation #for special char
    
    characters=letters
    if number:
        characters+=digits #if number is true 
    if special_char:
        characters+=special # if special_char is true
    
    password=""
    all_criteria=False
    has_number=False
    has_specials=False
    
    while not all_criteria or len(password) < length:
        new_character=random.choice(characters)# selects character randomly
        password+=new_character
    
    # this conditional statements check if we have number and special char 
        if new_character in digits:
            has_number=True 
        elif new_character in special:
            has_specials=True 
            
        all_criteria=True
        if number: # if number is true
            all_criteria=has_number #then all critia and has number is true 
        if special_char: # if special is true
            all_criteria=all_criteria and has_specials # then all criteria checks if it has number and special 
            #if it does then return generated password
    
    return password
        
    
    
length=int(input("enter ther length of pass: "))
has_number=input("do u want number(y/n): ").lower() == "y" #if true number is true 
has_special=input("do u want special(y/n): ").lower() == "y" #if true char is true 
pwd=gen_pass(length,has_number,has_special)
print(pwd)