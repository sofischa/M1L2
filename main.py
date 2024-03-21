import random
elements = "<>,.?/*!#$%^&_-=+@qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
pass_length = int(input("Введите длину пароля: "))

password = ""
for i in range(pass_length):
    password += random.choice(elements)

print(password)
