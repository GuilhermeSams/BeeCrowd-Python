'''Faça um programa que leia cinco valores inteiros. Conte quantos desses valores são pares, ímpares, positivos e negativos. Imprima essas informações como o exemplo a seguir.

Entrada
A entrada será 5 valores inteiros.

Saída
Imprima uma mensagem como o exemplo a seguir com todas as letras em minúsculas, indicando quantos  desses valores são pares, ímpares, positivos e negativos.'''
cont_par = 0
cont_impar = 0
cont_positivo = 0
cont_negativo = 0
for n in range(1,6):
    num = int(input())
    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
    if num > 0:
        cont_positivo += 1
    elif num < 0:
        cont_negativo += 1
print(f'{cont_par} valor(es) par(es)')
print(f'{cont_impar} valor(es) impar(es)')
print(f'{cont_positivo} valor(es) positivo(s)')
print(f'{cont_negativo} valor(es) negativo(s)')