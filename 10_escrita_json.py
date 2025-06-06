import json

pessoa = {
    'nome': 'Timóteo Gandolberto Liminha',
    'idade': 95,
    'email': 'l33tg4m3r@gmail.com'
}

with open("saida.json", "w") as arq:
    json.dump(pessoa, arq, indent=4)