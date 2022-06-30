A, B, C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)

pi = 3.14159

c1 = (A * C) / 2
c2 = pi * (C ** 2)
c3 =  ((A + B)  * C) / 2
c4 = B ** 2
c5 =  A * B

print(f'TRIANGULO: {c1:.3f}\nCIRCULO: {c2:.3f}\nTRAPEZIO: {c3:.3f}\nQUADRADO: {c4:.3f}\nRETANGULO: {c5:.3f}')

'''Faça um programa que leia três valores de ponto flutuante: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem base A e altura C.
b) a área do círculo do raio C. (pi = 3,14159)
c) a área do trapézio que tem A e B por base e C por altura.
d) a área do quadrado que possui o lado B.
e) a área do retângulo que possui os lados A e B.

Entrada
O arquivo de entrada contém três valores duplos com um dígito após a vírgula decimal.

Saída
O arquivo de saída deve conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com uma
 mensagem correspondente (em português) e um espaço entre os dois pontos e o valor. O valor calculado deve ser 
 apresentado com 3 dígitos após a casa decimal.'''