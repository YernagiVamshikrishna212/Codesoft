import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol = '()[]{};#*._'
number = '0123456789'

all = lower + upper + number + symbol
length = 10
password = "".join(random.sample(all, length))

print("The Generated Password is:", password)
