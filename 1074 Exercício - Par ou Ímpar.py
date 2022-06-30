'''Leia um valor inteiro N .
Depois, leia esses N valores e imprima uma mensagem para cada valor dizendo se esse valor é ímpar , par , positivo ou negativo .
Em caso de zero (0), embora a descrição correta seja "EVEN NULL", pois por definição zero é par, seu programa deve imprimir apenas "NULL", sem aspas.'''



N = int(input())
X = ['']

for i in range(1, N + 1):
    X.append(int(input()))

for i in range(1, N + 1):
    if X[i] > 0:
        if X[i] % 2 == 0:
            print("MESMO POSITIVO")
        else:
            print("IMPAR POSITIVO")

    if X[i] == 0:
        print("NULLO")

    if X[i] < 0:
        if X[i] % 2 == 0:
            print("MESMO NEGATIVO")
    else:
        print("IMPAR NEGATIVO")