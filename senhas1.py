import string
from itertools import combinations_with_replacement
from random import random, choice

def gerar_senhas(valores, tamanho):
    comb = combinations_with_replacement(valores, tamanho)
    a = list(comb)

    print(a)
    print("--------------------------------------------")
    print("A lista contém: ", len(a), "itens")

valores = 'abcd'
gerar_senhas(valores, 3)

#print(len(gerar_senhas(valores, 3)))


    

