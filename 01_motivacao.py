"""
Teste de desempenho: buscar números em um grupo de 10.000.000 de números
"""
import random

QT = 10000000

def realiza_buscas(dados):
    print("Início")
    for i in range(1000):
        num = random.randint(0, QT-1)
        if num in dados:
            print(i, " -> procurando por", num, "\t:", end='')
            print(" Achou")
        
    print("Fim.\n")

print("** Teste 1 - utilizando uma lista **\n")
dados = list(range(QT))
input("Qualquer tecla para iniciar...")
realiza_buscas(dados)

input()
print("** Teste 2 - utilizando um conjunto **\n")
dados = set(range(QT))
input("Qualquer tecla para iniciar...")
realiza_buscas(dados)