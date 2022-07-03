"""Você deve fazer um programa que leia um número de ponto flutuante e imprimir uma mensagem dizendo
a qual dos seguintes intervalos o número pertence: [0,25] (25,50], (50,75], (75,100].
número for menor que zero ou maior que 100, o programa deve imprimir a mensagem “Fora de intervalo” que significa "Fora
do Intervalo".

O símbolo '(' representa maior que. Por exemplo:
[0,25] indica números entre 0 e 25,0000, incluindo ambos.
(25,50] indica números maiores que 25 (25,00001) até 50,0000000.

Entrada
O arquivo de entrada contém um número de ponto flutuante.

Saída
A saída deve ser uma mensagem como o exemplo a seguir."""

num = float(input())

if 0 <= num <= 25:
    print("Intervalo [0,25]")
elif 25 < num <= 50:
    print("Intervalo (25,50]")
elif 50 < num <= 75:
    print("Intervalo (50,75]")
elif 75 < num <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
