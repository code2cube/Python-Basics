import random

while True:

    def password():
        length = input("How many characters do you want your password to be?\n")

        if int(length) > 94:
            print("================================================\nMust be less than 95 characters\n================================================")

        else:
            lower = "abcdefghijklmmnopqrstuvwxyz"
            upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            numbers = "1234567890"
            symbols = "~`!@#$%^&*()_+-={}[]';<>?,./|\:"

            password = "".join(random.sample(lower + upper + numbers + symbols, int(length)))
            print(f"Your new password is\n {password}")
            print("================================================\nMade by Samuel Sharivker\n================================================")
    password()
