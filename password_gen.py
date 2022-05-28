import random

q1 = input("How many passwords do you need?\n")
ask = input("How many characters do you want the passwords to be?\n")

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers = "1234567890"
symbols = "~`!@#$%^&*()_+-={}[]\|;:<>,.?/'"

l = int(q1) + int(1)

for x in range(1, l):
    password = "".join(random.sample(lower + upper + numbers + symbols, int(ask)))
    print(f"{x}. " + str(password))
