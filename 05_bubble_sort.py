# Bubble sort
def ordenar(vet):
    N = len(vet)
    for j in range(N): # repete N vezes
        trocou = False # saber se foi feita ao menos 1 troca

        for i in range(1, N - j):
            # compara par a par, trocando se estiver fora de ordem
            if vet[i - 1] > vet[i]:
                vet[i - 1], vet[i] = vet[i], vet[i - 1]
                trocou = True
        
        if not trocou:
            break

# exemplo
valores = [15, 17, 2, 18, 4]
ordenar(valores)
print(valores)