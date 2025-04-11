def busca_binaria(vetor, alvo):
    menor, meio, maior = 0, 0, len(vetor) - 1
 
    while menor <= maior: 
        meio = (menor + maior) // 2

        if vetor[meio] < alvo:
            menor = meio + 1
        elif vetor[meio] > alvo:
            maior = meio - 1
        else:
            return True
 
    return False

r = busca_binaria([1, 4, 5, 7, 9, 15, 21, 34, 54, 100], 5)
print(r)