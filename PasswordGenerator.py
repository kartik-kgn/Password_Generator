
import random
chars = "abcdefghijklmnopqrstuvwxyz123456789@#$%&*!"
length = int(input("enter length :"))
password = ""
for a in range(length):
     password+= random.choice(chars)

print(password)