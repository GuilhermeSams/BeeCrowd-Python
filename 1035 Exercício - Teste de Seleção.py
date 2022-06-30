'''Leia 4 valores inteiros A, B, C e D. Então, se
B for maior do que C e D for maior do que A e se a soma de C e D for maior do que a soma de A e B e se C e D forem valores positivos e se A for par,
escreva a mensagem “Valores aceitos” (Valores aceitos). Caso contrário, escreva a mensagem “Valores nao aceitos” (Valores não aceites).

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostra a mensagem correspondente após a validação dos valores.'''

A, B, C, D = map(int, input().split(" "))

if B > C and D > A and C + D > A + B and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")