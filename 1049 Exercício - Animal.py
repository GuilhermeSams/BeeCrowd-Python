'''Nesse problema, seu trabalho é ler três palavras em português. Essas palavras definem um animal de acordo com a tabela abaixo, da esquerda para a direita. Em seguida, imprima o animal escolhido definido por essas três palavras.

Entrada
A entrada contém 3 palavras, uma por linha, que serão utilizadas para identificar o animal, conforme tabela acima, todas com letras minúsculas.

Saída
Imprima o nome do animal de acordo com a entrada fornecida.'''

animal = str(input())
sub_classe = str(input())
ramo = str(input())

if animal == 'vertebrado':
    if sub_classe == 'ave':
        if ramo == 'carnivoro':
            print("aguia")
        else:
            print("pomba")
    elif sub_classe == 'mamifero':
        if ramo == 'onivoro':
            print('homem')
        elif ramo == 'herbivoro':
            print("vaca")
elif animal == 'invertebrado':
    if sub_classe == 'inseto':
        if ramo == 'hematofago':
            print("pulga")
        else:
            print("lagarta")
    elif sub_classe == 'anelideo':
        if ramo == 'hematofago':
            print("sanguessuga")
        else:
            print("minhoca")