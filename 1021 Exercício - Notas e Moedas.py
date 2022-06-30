"""Leia um valor de ponto flutuante com duas casas decimais. Isso representa um valor monetário.
Depois disso, calcule o menor número possível de notas e moedas nas quais o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0,50, 0,25, 0,10, 0,05 e 0,01.
Imprima a mensagem “NOTAS:” seguida da lista de notas e a mensagem “MOEDAS:” seguida da lista de moedas.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000,00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para alterar o valor inicial, conforme o exemplo dado."""

reais, centavo = map(int, input().split("."))
centavo += reais * 100

calc_100 = centavo // 10000
centavo %= 10000

calc_50 = centavo // 5000
centavo %= 5000

calc_20 = centavo // 2000
centavo %= 2000

calc_10 = centavo // 1000
centavo %= 1000

calc_5 = centavo // 500
centavo %= 500

calc_2 = centavo // 200
centavo %= 200


print('NOTAS:')
print(f'{int(calc_100)} nota(s) de R$ 100.00')
print(f'{int(calc_50)} nota(s) de R$ 50.00')
print(f'{int(calc_20)} nota(s) de R$ 20.00')
print(f'{int(calc_10)} nota(s) de R$ 10.00')
print(f'{int(calc_5)} nota(s) de R$ 5.00')
print(f'{int(calc_2)} nota(s) de R$ 2.00')


calc_1 = centavo // 100
centavo %= 100

calc_0_50 = centavo // 50
centavo %= 50

calc_0_25 = centavo // 25
centavo %= 25

calc_0_10 = centavo // 10
centavo %= 10

calc_0_05 = centavo // 5
centavo %= 5

calc_0_01 = centavo // 1
centavo %= 1

print('MOEDAS:')
print(f'{int(calc_1)} moeda(s) de R$ 1.00')
print(f'{int(calc_0_50)} moeda(s) de R$ 0.50')
print(f'{int(calc_0_25)} moeda(s) de R$ 0.25')
print(f'{int(calc_0_10)} moeda(s) de R$ 0.10')
print(f'{int(calc_0_05)} moeda(s) de R$ 0.05')
print(f'{int(calc_0_01)} moeda(s) de R$ 0.01')
