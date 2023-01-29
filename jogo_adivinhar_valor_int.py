#jogo_adivinhar_valor_int
"""
    Autor: Michel Brito
    Descrição: Jogo de adivinhar um valor entre 1 e 10.
"""

import random

valor = random.randint(1, 10)
pontuacao_max = 100
tentativas = 0

print('Adivinhe um valor de 1 a 10 (inteiros).')

while True:
    numero = int( input('Informe um número inteiro de 1 a 10: ') )
    tentativas += 1
    if numero < valor:
        print('O valor exato é maior.')
    elif numero > valor:
        print('O valor exato é menor.')
    elif numero == valor:
        print(f'Parabéns! Você acertou o valor exato, {valor}!')
        print('Foram {} tentativas e a sua pontuação é {}.'.format( tentativas, format((pontuacao_max / tentativas), '.2f')) )
        break

print('Partida encerrada.')