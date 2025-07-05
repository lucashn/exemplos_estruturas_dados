class No:
    def __init__(self, valor, prox):
        self.valor = valor
        self.prox = prox

class Lista:
    def __init__(self):
        self.head = None

    def inserir_fim(self, valor):
        novo = No(valor, None)

        if self.head == None:
            # lista estava vazia
            self.head = novo
        else:
            # percorrer a lista até chegar no último nó
            atual = self.head
            while atual.prox != None:
                atual = atual.prox
            
            # adiciona no final
            atual.prox = novo

    def inserir(self, i, valor):
        if i == 0: # trocar a cabeça
            self.head = No(valor, self.head)
        else:
            atual = self.head

            for _ in range(i-1):
                atual = atual.prox
            
            atual.prox = No(valor, atual.prox)

    def imprimir(self):
        atual = self.head
        print('[ ', end='')
        while atual != None:
            print(atual.valor, end=' ')
            atual = atual.prox
        print(']')

    def tamanho(self):
        qt = 0
        atual = self.head

        while atual != None:
            atual = atual.prox
            qt += 1

        return qt

    def recuperar(self, i):
        atual = self.head

        for _ in range(i):
            atual = atual.prox
        
        return atual.valor
    
    def buscar(self, alvo):
        atual = self.head

        while atual != None:
            if atual.valor == alvo:
                return True
            
            atual = atual.prox
        
        return False
    
    def remover(self, i):
        if i == 0: # remover a cabeça
            self.head = self.head.prox
        else:
            atual = self.head

            for _ in range(i-1):
                atual = atual.prox
            
            atual.prox = atual.prox.prox

numeros = Lista()
numeros.inserir_fim(5)
numeros.inserir_fim(10)
numeros.inserir_fim(13)

assert numeros.tamanho() == 3
assert numeros.recuperar(0) == 5
assert numeros.recuperar(1) == 10
assert numeros.recuperar(2) == 13

numeros.imprimir()
numeros.inserir(i=3, valor=100)
numeros.imprimir()

numeros.remover(0)
numeros.remover(2)
numeros.imprimir()

print(numeros.buscar(10))
print(numeros.buscar(80))

print("Tudo ok")