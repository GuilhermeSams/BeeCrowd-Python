'''Escreva um programa que leia dois números X e Y e imprima o resultado da divisão de X por Y.
Caso não seja possível, imprima a mensagem "divisão impossivel".'''
calc = 0
num1 = num2 = 1
N = int(input())
for c in range (N):
        num1, num2 = map(int, input().split(" "))
        if num2 != 0:
            calc = num1 / num2
            print(calc)
        else:
            print("divisao impossivel")
