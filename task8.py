import random
import string
def func(n):
    password = ''
    pswrd = string.ascii_letters + string.digits + string.punctuation
    for i in range(n):
        password += random.choice(pswrd)
    return password

print(func(int(input())))