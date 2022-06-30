'''Leia 3 números de ponto flutuante. Depois, imprima as raízes da fórmula de bhaskara.
Se for impossível calcular as raízes devido a uma
divisão por zero ou raiz quadrada de um número negativo, apresenta a mensagem “Impossível calcular” .

Entrada
Leia 3 números de ponto flutuante (duplo) A, B e C.

Saída
Imprima o resultado com 5 dígitos após a vírgula decimal ou a mensagem se for impossível calcular.'''
from math import sqrt

A, B, C = map(float, input().split())
delta = B ** 2 - 4 * A * C
if A ==0 or delta < 0:
    print("Impossivel calcular")
else:
    print(f'R1 = {( - B + sqrt(delta)) / (2 * A):.5f}')
    print(f'R2 = {( - B  - sqrt(delta)) / (2 * A):.5f}')

