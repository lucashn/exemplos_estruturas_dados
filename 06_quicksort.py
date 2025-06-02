def qs(vet):
    if len(vet) <= 1: return vet            # já está ordenada
    pivo, resto = vet[0], vet[1:]           # separando pivô do resto
    esq = [x for x in resto if x <= pivo]   # lista da esquerda
    dir = [x for x in resto if x > pivo]    # lista da direita
    return qs(esq) + [pivo] + qs(dir)

print(qs([5, 3, 8, -2, 0, 4, 4, 1]) )