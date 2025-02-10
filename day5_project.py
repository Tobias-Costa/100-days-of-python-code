import random

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers_list = [0,1,2,3,4,5,6,7,8,9]

symbols_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Bem vindo ao meu gerador de senhas com Python")
nr_letters = int(input("Quantas letras quer ter na sua senha?\n"))
nr_numbers = int(input("Quantos números quer ter na sua senha?\n"))
nr_symbols = int(input("Quantos símbolos quer ter na sua senha?\n"))

password_list = []
password = ""

for i in range(nr_letters):
    password_list.append(random.choice(letters_list))

for i in range(nr_numbers):
    password_list.append(random.choice(numbers_list))

for i in range(nr_symbols):
    password_list.append(random.choice(symbols_list))

random.shuffle(password_list)
for item in password_list:
    password += str(item)

print(f"Sua senha é: {password}")