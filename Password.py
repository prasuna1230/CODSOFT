import string
import random
length=int(input("Enter the length of password:"))
lower_length=int(input("Enter the number of lowercase characters:"))
upper_length=int(input("Enter the number of uppercase characters: "))
digit_length=int(input("Enter the number of digits: "))
symbol_length=int(input("Enter tne number of symbols: "))
pwd_len=lower_length+upper_length+digit_length+symbol_length
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digits
symbol=string.punctuation
str=random.choices(lower,k=lower_length)+random.choices(upper,k=upper_length)+random.choices(digit,k=digit_length)+random.choices(symbol,k=symbol_length)
random.shuffle(str)
password="".join(str)
print("password is: ",password)
