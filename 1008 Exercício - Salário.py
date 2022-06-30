'''Escreva um programa que leia o número do funcionário, o número de horas trabalhadas em um mês e o valor que ele recebeu por hora. Imprima o número do funcionário e o salário que receberá no final do mês, com duas casas decimais.

Não se esqueça de imprimir o final da linha após o resultado, caso contrário você receberá “Erro de apresentação”.
Não se esqueça do espaço antes e depois do sinal de igual e depois do U $.
Entrada
O arquivo de entrada contém 2 números inteiros e 1 valor de ponto flutuante, representando o número, a quantidade de horas trabalhadas e a quantidade que o funcionário recebe por hora trabalhada.

Saída
Imprima o número e o salário do funcionário, conforme o exemplo dado, com um espaço em branco antes e depois do sinal de igual.'''




n1 = int(input(""))
n2 = int(input(""))
h = float(input(""))

salario = n2 * h

print(f'NUMBER = {n1}')
print(f'SALARY = U$ {salario:.2f}')
