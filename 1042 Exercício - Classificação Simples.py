'''Leia três inteiros e classifique-os em ordem crescente.
Em seguida, imprima esses valores em ordem crescente, uma linha em branco e a seguir os valores na seqüência conforme foram lidos.

Entrada
A entrada contém três números inteiros.

Saída
Apresente a saída conforme solicitado acima.'''

n1, n2, n3 = map(int, input().split())

lista = [n1, n2, n3]
lista.sort()
print(f'{lista[0]}\n{lista[1]}\n{lista[2]}')
print(f'\n{n1}\n{n2}\n{n3}')