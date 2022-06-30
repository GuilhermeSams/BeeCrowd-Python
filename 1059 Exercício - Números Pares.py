'''Escreva um programa que imprima todos os números pares entre 1 e 100, incluindo-os se for o caso.

Entrada
Neste problema extremamente simples, não há entrada.

Saída
Imprima todos os números pares entre 1 e 100, incluindo-os, um por linha.'''

for cont in range(2, 101):
    if cont % 2 == 0:
        print(cont)