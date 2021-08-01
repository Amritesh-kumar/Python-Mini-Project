import random

print('Welcome to Password Generator!')
length = int(input('Enter your password length: '))

chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*123456789'
print('Here is your Password')

password = ''
for i in range(length):
    password += random.choice(chars)
    # print(password)

print(password)