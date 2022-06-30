'''A empresa ABC decidiu dar um aumento salarial aos seus funcionários, de acordo com a tabela a seguir:

Salário	Taxa de reajuste
0 - 400,00
400,01 - 800,00
800,01 - 1200,00
1200,01 - 2000,00
Acima de 2.000,00

15%
12%
10%
7%
4%

Leia o salário do funcionário, calcule e imprima o salário do novo funcionário, bem como o dinheiro ganho e o aumento percentual obtido pelo funcionário, com as respectivas mensagens em português, conforme exemplo abaixo.
Entrada
A entrada contém apenas um número de vírgula flutuante, com 2 dígitos após a vírgula decimal.

Saída
Imprima 3 mensagens seguidas dos números correspondentes (ver exemplo) informando o novo salário, a proporção do dinheiro ganho e o percentual obtido pelo funcionário. Nota:
Novo salario:  significa "Novo Salário "
Reajuste ganho: significa "Dinheiro ganho"
Em percentual: significa "Em percentagem"'''

salario = float(input())

if salario  >= 0 and salario <= 400:
    novo_salario = salario + (salario * 15 / 100)
    reajuste = novo_salario - salario
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 15 %')
elif salario >= 400.01 and salario <= 800:
    novo_salario = salario + (salario * 12 / 100)
    reajuste = novo_salario - salario
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 12 %')
elif salario >= 800.01 and salario <=1200:
    novo_salario = salario + (salario * 10 / 100)
    reajuste = novo_salario - salario
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print("Em percentual: 10 %")
elif salario >=1200.01 and salario <=2000:
    novo_salario = salario + (salario * 7 / 100)
    reajuste = novo_salario - salario
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print("Em percentual: 7 %")
else:
    novo_salario = salario + (salario * 4 / 100)
    reajuste = novo_salario - salario
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print("Em percentual: 4 %")