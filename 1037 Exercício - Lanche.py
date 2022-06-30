'''Usando a tabela a seguir, escreva um programa que leia um código e a quantidade de um item.
Depois imprima o valor a pagar. Este é um programa muito simples com o único propósito de praticar os comandos de seleção.

Entrada
O ficheiro de entrada contém dois números inteiros X e Y . X é o código do produto e Y é a quantidade deste item de acordo com a tabela acima.

Saída
A saída deve ser a mensagem “Total: R $” seguida do valor total a ser pago, com 2 dígitos após a casa decimal.'''


X, Y = map(int, input().split())

if X == 1:
    print(f'Total: R$ {Y * 4:.2f}')
elif X == 2:
    print(f'Total: R$ {Y * 4.50:.2f}')
elif X == 3:
    print(f'Total: R$ {Y * 5:.2f}')
elif X == 4:
    print(f'Total: R$ {Y * 2:.2f}')
elif X == 5:
    print(f'Total: R$ {Y * 1.50:.2f}')