'''Leia a hora de início e de término de um jogo, em horas. Em seguida, calcule a duração do jogo, sabendo que o jogo pode começar em um dia e terminar em outro, com duração máxima de 24 horas. A mensagem deve ser impressa em português “O JOGO DUROU X HORA (S)” que significa “O JOGO DURADO X HORA (S)”

Entrada
Dois números inteiros que representam a hora de início e de término de um jogo.

Saída
Imprima a duração do jogo como na saída de amostra.'''

hora_inicio, hora_termino = map(int, input().split())

if hora_termino > hora_inicio:
    print(f'O JOGO DUROU {hora_termino - hora_inicio} HORA(S)')
else:
    print(f'O JOGO DUROU {abs(hora_inicio - 24 - hora_termino)} HORA(S)')