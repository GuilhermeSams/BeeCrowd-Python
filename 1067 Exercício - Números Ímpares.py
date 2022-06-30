'''Leia um valor inteiro X (1 <= X <= 1000). Em seguida, imprima os números ímpares de 1 a X , cada um em uma linha, incluindo X se for o caso.

Entrada
A entrada será um valor inteiro.

Saída
Imprime todos os valores ímpares entre 1 e X , incluindo X se for o caso.'''
X = int(input())

for c in range(1, X+1):
    if c % 2 != 0:
        print(c)