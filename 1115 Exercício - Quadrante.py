'''Escreva um programa para ler as coordenadas (X, Y) de um número indeterminado de pontos no sistema cartesiano.
Para cada ponto escreva o quadrante ao qual ele pertence.
O programa termina quando pelo menos uma das duas coordenadas é NULL (nesta situação sem escrever nenhuma mensagem).'''
x = y = 1
while x != 0 and y != 0:
    x, y = map(int, input().split(" "))
    if x > 0 and y > 0:
        print("primeiro")
    elif x < 0 and y > 0:
        print("segundo")
    elif x < 0 and y < 0:
        print("terceiro")
    elif x > 0 and y < 0:
        print("quarto")