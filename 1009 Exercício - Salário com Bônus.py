'''Faça um programa que leia o nome do vendedor, seu salário fixo e o valor total da venda feita por ele mesmo no mês (em dinheiro). Considerando que esse vendedor recebe 15% sobre todos os produtos vendidos, escreva o salário final (total) desse vendedor no final do mês, com duas casas decimais.

- Não se esqueça de imprimir o final da linha após o resultado, caso contrário receberá “ Erro de apresentação ”.

- Não se esqueça dos espaços em branco.

Entrada
O arquivo de entrada contém um texto (nome do funcionário) e dois valores de precisão dupla, que são o salário do vendedor e o valor total vendido por ele.

Saída
Imprime o salário total do vendedor, conforme o exemplo dado.

Amostras de entrada	'''

name = str(input("employee's first name: "))
salario = float(input(""))
venda_total = float(input(""))


calc_total = (venda_total * 15) / 100
calc = calc_total + salario


print(f'TOTAL = R${calc:.2f}')