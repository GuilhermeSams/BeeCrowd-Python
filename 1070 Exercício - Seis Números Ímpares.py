'''Leia um valor inteiro X e imprima os 6 números ímpares consecutivos de X , um valor por linha, incluindo X se for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.'''

X = int(input())
for c in range(0, 12):
    if X % 2 != 0:
        print(X)
    X = X + 1