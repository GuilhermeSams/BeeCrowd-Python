'''Leia um valor inteiro, que é a duração em segundos de um determinado evento em uma fábrica, e informe-o expresso
em horas: minutos: segundos.

Entrada
O ficheiro de entrada contém um número inteiro N .

Saída
Imprime o tempo de leitura no arquivo de entrada (segundos) convertido em horas: minutos: segundos como no exemplo a seguir.'''


N = int(input())

horas = N // (60 ** 2)
N = N - horas * (60**2)

minutos = N // 60
N = N - (minutos * 60)

segundos = N

print(f'{horas:.0f}: {minutos:.0f}: {segundos:.0f}' )
















