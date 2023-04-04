import random
import string

def gen_pass(length,number,special_char):
    letters=string.ascii_letters # for alphabelts
    digits=string.digits # for numbers
    special=string.punctuation #for special char
    
    password=""
    
    while len(password) < length:
        
        if number and len(password) < length :
            password += random.choice(digits)
        if special_char and len(password) < length :
            password += random.choice(special)
        if len(password) < length:
            password+= random.choice(letters)
    
    return password
   
length=int(input("enter ther length of pass: "))
has_number=input("do u want number(y/n): ").lower() == "y" 
has_special=input("do u want special(y/n): ").lower() == "y"
pwd=gen_pass(length,has_number,has_special)
print(pwd)
