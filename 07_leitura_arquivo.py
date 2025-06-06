# abre o arquivo no modo leitura
with open("poesia.txt") as arq:
    # percorre o arquivo linha por linha, imprimindo o # da linha e seu conteúdo
    for i, linha in enumerate(arq, start=1):
        print(i, linha.strip()) # remove o pulo de linha e os espaços no final da string

# nota: o arquivo é fechado automaticamente ao sair do escopo (fora do bloco do 'with')