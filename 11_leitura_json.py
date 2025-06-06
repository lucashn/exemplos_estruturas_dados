import json

with open('saida.json') as arq:
    dados = json.load(arq)
    print(dados)

