'''Num país imaginário chamado Lisarb, todas as pessoas ficam muito felizes em pagar seus impostos porque sabem que não existem políticos corruptos e os impostos são usados ​​para beneficiar a população, sem qualquer apropriação indébita. A moeda desse país é a Rombus, cujo símbolo é R $.

Leia um valor com 2 dígitos após a vírgula decimal, equivalente ao salário de um habitante de Lisarb. A seguir imprima o valor devido que esta pessoa deve pagar dos impostos, conforme tabela abaixo.

Lembre-se, se o salário for de R $ 3.002,00 por exemplo, a alíquota de 8% é apenas acima de R $ 1.000,00, pois o salário de R $ 0,00 a R $ 2.000,00 é isento de impostos. No exemplo a seguir, a alíquota total é de 8% sobre R $ 1.000,00 + 18% sobre R $ 2,00, resultando em R $ 80,36 ao todo. A resposta deve ser impressa com 2 dígitos após a vírgula decimal.

Entrada
A entrada contém apenas um número de ponto flutuante, com 2 dígitos após o ponto decimal.

Saída
Imprima a mensagem “R $” seguida de um espaço em branco e o valor total do imposto a pagar, com dois dígitos após a vírgula decimal. Se o valor for até 2.000, imprime a mensagem "Isento".'''

salario = float(input())
calc_taxa = (salario / 8)
print(calc_taxa)

