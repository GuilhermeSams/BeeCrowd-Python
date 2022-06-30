'''Leia 6 valores que podem ser números de ponto flutuante. Depois imprima quantos deles foram positivos.
Na próxima linha, imprima a média de todos os valores positivos digitados, com um dígito após a vírgula decimal.

Entrada
A entrada consiste em 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um número será positivo.

Saída
O primeiro valor de saída é a quantidade de números positivos. A próxima linha deve mostrar a média dos valores positivos digitados.'''
cont = 0
soma = 0
media = 0
for c in range(1, 7):
    num = float(input())
    if num >= 0:
        cont += 1
        soma += num
        media = soma / cont
print(f'{cont} valores positivos')
print(f'{media:.1f}')

