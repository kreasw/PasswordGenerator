import random

letters_lower = "abcdefghijklmnopqrstuvwxyz"
letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
numbers = "0123456789"

length = int(input("what should be the length?: "))
password = ""

everything = letters_upper + letters_lower + symbols + numbers # creates a full string

for i in range(length):
    password += random.choice(everything)
    
print("random password: ", password)
