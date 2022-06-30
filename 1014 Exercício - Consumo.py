'''Calcule o consumo médio de um carro levando em consideração a distância total percorrida (em Km) e o total de
combustível gasto (em litros).

Entrada
O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total (em Km) e o segundo é
um número de ponto flutuante Y  representando o total de combustível irradiado, com um dígito após o ponto decimal.

Saída
Apresente um valor que represente o consumo médio de um carro com 3 dígitos após a vírgula, seguido da mensagem “km / l”.'''

X = int(input())
Y = float(input())

calc =  X / Y

print(f'{calc:.3f} km/l')