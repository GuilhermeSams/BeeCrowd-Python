'''A fórmula para calcular a área de uma circunferência é definida como A = π. R 2 . Considerando este problema que π = 3,14159 :

Calcule a área usando a fórmula fornecida na descrição do problema.

Entrada
A entrada contém um valor de ponto flutuante (precisão dupla), que é a variável R .

Saída
Apresente a mensagem "A =" seguida do valor da variável, como no exemplo abaixo, com quatro casas decimais após a vírgula. Use todas as variáveis ​​de precisão dupla. Como todos os problemas, não se esqueça de imprimir o final da linha após o resultado, caso contrário, receberá "Erro de apresentação".'''

R = float(input("Digite um valor: "))

A = 3.14159 * R ** 2

print(f'A={A:.4f}')
