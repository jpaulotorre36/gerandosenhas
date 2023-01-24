import string
from random import random, choice

valores = string.ascii_letters + string.digits + string.punctuation

#print(valores)
tamanho = 5
senha = ""

for i in range(tamanho):
    senha += choice(valores)

print(senha)




