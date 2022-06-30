'''Leia um número inteiro entre 1 e 12, incluindo. Correspondente a este número, deve-se imprimir o mês do ano, em inglês, com a primeira letra em maiúscula.

Entrada
A entrada contém apenas um número inteiro.

Saída
Imprima o nome do mês de acordo com o número inserido, com a primeira letra em maiúscula.'''

mes = int(input())

if mes == 1:
    print("January")
elif mes == 2:
    print("February")
elif mes == 3:
    print("March")
elif mes == 4:
    print("April")
elif mes == 5:
    print("May")
elif mes == 6:
    print("June")
elif mes == 7:
    print("July")
elif mes == 8:
    print("August")
elif mes == 9:
    print("September")
elif mes == 10:
    print("October")
elif mes == 11:
    print("November")
else:
    print("December")