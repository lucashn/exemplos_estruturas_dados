# Selection sort
def ordenar(vet):
    N = len(vet)
    for i in range(N):

        # procura o menor elemento entre as posições i e N-1
        menor = i
        for j in range(i, N):
            if vet[j] < vet[menor]:
                menor = j
        
        # coloca o menor elemento encontrado na sua posição
        vet[i], vet[menor] = vet[menor], vet[i]

# exemplo
valores = [15, 17, 2, 18, 4]
ordenar(valores)
print(valores)

