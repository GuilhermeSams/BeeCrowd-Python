'''Leia os valores flutuantes de três pontos (A, B e C) e verifique se é possível fazer um triângulo com eles.
Se for possível, calcule o perímetro do triângulo e imprima a mensagem:

Perimetro = XX.X

Se não for possível, calcule a área do trapézio que tem como base A e B e C a altura, e imprima a mensagem:
Área = XX.X
Entrada
O arquivo de entrada possui números de ponto flutuante em árvore.
Saída
Imprima o resultado com um dígito após a vírgula decimal.'''

A, B , C = map(float, input().split()) #não esta splitado porque o bee crowd não aceita
if A < B + C and B < A + C and C < A + B:
    perimetro = (A + B + C)
    print(f'Perimetro = {perimetro}')
else:

    print(f"Area = {C * (A + B) / 2}")