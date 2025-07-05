# abre o arquivo no modo leitura
with open("poesia.txt") as arq:
    # percorre o arquivo linha por linha, imprimindo o # da linha e seu conteúdo
    for linha in arq:
        print(linha.strip())

# nota: o arquivo é fechado automaticamente ao sair do escopo (fora do bloco do 'with')