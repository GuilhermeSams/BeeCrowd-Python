'''Leia um número inteiro que é o número do código para discagem telefônica.
Em seguida, imprima o destino de acordo com a seguinte tabela:

Caso o número da entrada não seja encontrado na tabela acima, o resultado deve ser:
DDD nao cadastrado
Significa “DDD não encontrado” na língua portuguesa.

Entrada
A entrada consiste em um número inteiro único.

Saída
Imprima o nome da cidade correspondente ao DDD de entrada.
mprime DDD nao cadastrado se não existe DDD correspondente ao número digitado.'''

n = int(input())

if n == 61:
    print("Brasilia")
elif n == 71:
    print("Salvador")
elif n == 11:
    print("Sao Paulo")
elif n == 21:
    print("Rio de Janeiro")
elif n == 32:
    print("Juiz de Fora")
elif n == 19:
    print("Campinas")
elif n == 27:
    print("Vitoria")
elif n == 31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")