'''Leia 3 números duplos (A, B e C) representando os lados de um triângulo e organize-os em ordem decrescente, de modo que o lado A seja o maior dos três lados. Em seguida, determine o tipo de triângulo que eles podem fazer, com base nos seguintes casos, sempre escrevendo uma mensagem apropriada:
se A ≥ B + C, escreva a mensagem: NAO FORMA TRIANGULO
se A 2 = B 2 + C 2 , escreva a mensagem: TRIANGULO RETANGULO
se A 2 > B 2 + C 2 , escreva a mensagem: TRIANGULO OBTUSANGULO
se A 2 <B 2 + C 2 , escreva a mensagem: TRIANGULO ACUTANGULO
se os três lados forem do mesmo tamanho, escreva a mensagem: TRIANGULO EQUILATERO
se apenas dois lados são iguais e o terceiro é diferente, escreva a mensagem: TRIANGULO ISOSCELES
Entrada
A entrada contém três números duplos, A (0 <A), B (0 <B) e C (0 <C).

Saída
Imprima todas as classificações do triângulo apresentadas na entrada.'''

A, B, C = map(float, input().split(" "))

lista = [A, B, C]
lista.sort()