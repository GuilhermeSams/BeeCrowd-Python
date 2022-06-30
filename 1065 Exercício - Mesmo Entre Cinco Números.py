'''Faça um programa que leia cinco valores inteiros . Conte quantos  desses valores são pares e imprima essas informações como no exemplo a seguir .

Entrada
A entrada será 5 valores inteiros.

Saída
Imprima uma mensagem como o exemplo a seguir com todas as letras em minúsculas, indicando quantos números pares foram digitados.'''
cont = 0
for n in range(1, 6):
    num = int(input())
    if num % 2 == 0:
        cont += 1
print(f'{cont} valores pares')
