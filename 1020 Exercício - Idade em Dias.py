'''Leia um valor inteiro correspondente à idade da pessoa (em dias) e imprima em anos, meses e dias,
seguido da respectiva mensagem “ano (s)”, “mes (s)”, “dia (s)”.

Nota: apenas para facilitar o cálculo, considere o ano
todo com 365 dias e 30 dias a cada mês. Nos casos de teste nunca haverá uma situação que permita 12 meses e alguns dias,
como 360, 363 ou 364. Este é apenas um exercício com o propósito de testar raciocínios matemáticos simples.

Entrada
O arquivo de entrada contém 1 valor inteiro.

Saída
Imprima a saída, como no exemplo a seguir.'''

idade = int(input())

calc_anos = idade // 365
calc_mes = (idade % 365) / 30
calc_dia = (idade % 365) % 30

calc_mes = int(calc_mes)
calc_dia = int(calc_dia)

print(f'{calc_anos} ano (s)')
print(f'{calc_mes} mes (s)')
print(f'{calc_dia} dia (s)')
