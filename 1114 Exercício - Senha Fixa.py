'''Escreva um programa que continue lendo uma senha até que ela seja válida.
Para cada senha errada lida, escreva a mensagem "Senha inválida".
Quando a senha for digitada corretamente imprima a mensagem "Acesso Permitido" e finalize o programa.
A senha correta é o número 2002.'''

senha_correta = 2002
senha = int(input())

while senha != 2002:
    print('Senha Invalida')
    senha = int(input())
print('Acesso Permitido')