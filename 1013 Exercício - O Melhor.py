a, b, c = map(int, input().split(" "))


MaiorAB = (int(a) + int(b) + abs(int(a) - int(b))) / 2
resultado = (int(MaiorAB) + int(c) + abs(int(MaiorAB) - int(c)))/2


print(f'{resultado:.0f} eh o maior')


'''Faça um programa que leia 3 valores inteiros e apresente o maior deles seguido da mensagem "eh o maior". Use a
seguinte fórmula:



Entrada
O arquivo de entrada contém 3 valores inteiros.

Saída
Imprima o maior destes três valores seguido de um espaço e da mensagem “eh o maior”.'''