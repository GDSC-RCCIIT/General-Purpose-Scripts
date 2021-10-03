# Password Generator

import random

length = int(input("Enter the length of the password: "))

if length >= 12 and length <= 25:

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    numbers = "0123456789"
    symbols = "[]{}()<>!@#$%^&*_+-=;:,./?"
    all = list(lower) + list(upper) + list(numbers) + list(symbols)

    rand_lower = random.choice(lower)
    rand_upper = random.choice(upper)
    rand_num = random.choice(numbers)
    rand_symbol = random.choice(symbols)
    temp_pass = rand_num + rand_upper + rand_lower + rand_symbol

    password = list(temp_pass) + random.sample(all, length - 4)
    random.shuffle(password)
    password = ''.join(password)
              
    print("\n", password, "\n")
else:
        print(" ** A strong password is at least 12-15 characters long. ** \n  ")
