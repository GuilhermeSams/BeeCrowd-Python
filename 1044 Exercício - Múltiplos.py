'''Leia dois valores nteger (A e B).
A seguir, o programa deve imprimir a mensagem "Sao Multiplos" (são múltiplos) ou
"Nao sao Multiplos" (não são múltiplos), correspondendo aos valores lidos.

Entrada
A entrada possui dois números inteiros.

Saída
Imprima a mensagem relativa à entrada conforme indicado acima.'''

A, B = map(int, input().split(" "))

A = int(A)
B = int(B)


if A > B:
    if A % B == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")

elif A < B:
    if B % A == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    print("Sao Multiplos")