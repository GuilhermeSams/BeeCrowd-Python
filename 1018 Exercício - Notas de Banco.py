'''Neste problema, você deve ler um valor inteiro e calcular o menor número possível de notas nas quais o valor pode ser decomposto.
As notas possíveis são 100, 50, 20, 10, 5, 2 e 1. Imprima o valor lido e a lista das notas.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N <1000000).

Saída
Imprima o número lido e a quantidade mínima de cada cédula necessária em língua portuguesa, conforme o exemplo dado.
 Não se esqueça de imprimir o final da linha após cada linha, caso contrário, você receberá “Erro de apresentação” .'''

num = int(input())
print(f'{num}')

calc100 = num // 100
num =  num - calc100 * 100

calc50 = num // 50
num = num - calc50 * 50

calc20 = num // 20
num = num - calc20 * 20

calc10 = num // 10
num = num - calc10 * 10

calc5 = num // 5
num = num - calc5 * 5

calc2 = num // 2
num = num - calc2 * 2

calc1= num // 1
num = num - calc1 * 1

print(f'{calc100} nota(s) de R$ 100,00')
print(f'{calc50} nota(s) de R$ 50,00')
print(f'{calc20} nota(s) de R$ 20,00')
print(f'{calc10} nota(s) de R$ 10,00')
print(f'{calc5} nota(s) de R$ 5,00')
print(f'{calc2} nota(s) de R$ 2,00')
print(f'{calc1} nota(s) de R$ 1,00')