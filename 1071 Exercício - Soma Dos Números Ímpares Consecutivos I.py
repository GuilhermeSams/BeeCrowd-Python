'''Leia dois valores inteiros X e Y . Imprima a soma de todos os valores ímpares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um número inteiro. Este número é a soma de todos os valores ímpares entre os dois valores de entrada que devem caber em um número inteiro.'''

soma = 0
X = int(input())
Y = int(input())
cont_x = min(X, Y)+1
cont_y = max(X, Y)
if cont_x % 2 == 0:
    cont_x += 1
for c in range(cont_x, cont_y, 2):
    soma += c
print(soma)