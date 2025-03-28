def busca_linear(vetor, alvo):
    for e in vetor:
        if e == alvo:
            return True

    return False

vet = [2, 4, 6, 8, 10]
print(busca_linear(vet, 8))