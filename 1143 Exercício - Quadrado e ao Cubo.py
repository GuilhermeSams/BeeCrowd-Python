"""Escreva um programa que leia um valor inteiro N (1 < N < 1000). Este N é a quantidade de linhas de saída que serão
apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido."""

lista_vaz = []

linha_saida = int(input())

for c in range(linha_saida):
    c += 1
    lista_vaz.append(c)

for num_c1 in lista_vaz:
    print(num_c1, end=" ")
    for n in lista_vaz:
        print(num_c1 * num_c1, end=" ")
        break
    for i in lista_vaz:
        print(num_c1 * num_c1 * num_c1)
        break
