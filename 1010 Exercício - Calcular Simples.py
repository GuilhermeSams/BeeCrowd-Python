'''Neste problema, a tarefa é ler o código de um produto 1, o número de unidades do produto 1, o preço de uma unidade do
 produto 1, o código de um produto 2, o número de unidades do produto 2 e o preço para uma unidade do produto 2. Após,
 calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores: dois inteiros e um valor flutuante com
 2 dígitos após a vírgula decimal.

Saída
O arquivo de saída deve ser uma mensagem como o exemplo a seguir, onde "Valor a pagar" significa Valor a pagar .
Lembre-se do espaço após ":" e após o símbolo "R $". O valor deve ser apresentado com 2 dígitos após o ponto.'''

cod1, unid2, valor3 = input().split(' ')
cod4, unid5, valor6 = input().split(' ')

cod1 = int(cod1)
unid2 = int(unid2)
cod4 = int(cod4)
unid5 = int(unid5)


valor3 = float(valor3)
valor6 = float(valor6)

calc1 = unid2 * valor3
calc2 = unid5 * valor6


print(f'VALOR A PAGAR: R$ {calc1 + calc2:.2f}')

