'''Escreva um programa que leia 6 números. Esses números serão apenas positivos ou negativos (desconsidere os valores nulos). Imprima o número total de números positivos.

Entrada
Seis números, positivos e / ou negativos.

Saída
Imprima uma mensagem com o número total de números positivos.'''
cont = 0
for n in range(0, 6):
    num = float(input())
    if num >= 0:
        cont += 1
print(f'{cont} valores positivos')