'''Leia 100 números inteiros. Imprima o valor de leitura mais alto e a posição de entrada.'''

lista = []
for c in range(5):
    n = int(input())
    lista += [n]
print(f'{max(lista)}')
print(lista.index(lista)+1)