'''Leia os quatro valores correspondentes aos eixos xey de dois pontos do plano, p1 (x1, y1) e p2 (x2, y2)
e calcule a distância entre eles, mostrando quatro casas decimais após a vírgula, de acordo com a fórmula :

Distância =

Entrada
O arquivo de entrada contém duas linhas de dados. O primeiro contém dois valores duplos:  x1 y1 e o segundo
também contém dois valores duplos com um dígito após a vírgula decimal: x2 y2 .

Saída
Calcule e imprima o valor da distância usando a fórmula fornecida, com 4 dígitos após o ponto decimal.

'''

from math import sqrt
x1, y1 = map(float, input().split(" "))
x2, y2 = map(float,input().split(" "))

Distancia = ((x2- x1)) **  2 + ((y2 - y1)) ** 2
raiz = sqrt(Distancia)


print(f'{raiz:.4f}')
a, b, c = map(float,input().split(" "))