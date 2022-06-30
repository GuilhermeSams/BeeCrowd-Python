'''Escreva um algoritmo que leia dois valores flutuantes (x e y), que devem representar as coordenadas de um ponto em um plano.
A seguir, determine a qual quadrante o ponto pertence ou se você está em um dos eixos cartesianos ou na origem (x = y = 0).

Se o ponto estiver na origem, escreva a mensagem "Origem".

Se o ponto está no eixo X escreva "Eixo X", senão se o ponto está no eixo Y escreva "Eixo Y".

Entrada
A entrada contém as coordenadas de um ponto.

Saída
A saída deve exibir o quadrante em que o ponto está.

Amostra de entrada	Amostra de saída
4,5 -2,2

Q4
'''

X, Y = map(float, input().split())

if X == Y ==0:
    print("Origem")
elif X == 0:
    print("Eixo Y")
elif Y == 0:
    print("Eixo X")
elif X > 0 and Y > 0:
    print("Q1")
elif Y > X and X < Y:
    print("Q2")
elif X < 0 and Y < 0:
    print("Q3")
elif X > 0 and Y < 0:
    print("Q4")