'''Leia 100 números inteiros. Imprima o valor de leitura mais alto e a posição de entrada.'''

maior_num = pos_maior = 0

for c in range(100):
    n = int(input())
    if n > maior_num:
        maior_num = n
        pos_maior = c

print(maior_num)
print(pos_maior + 1)
