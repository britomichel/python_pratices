#jogo_pedra_papel_tesoura_str
"""
    Autor: Michel Brito
    Descrição: Jogo Pedra/Papel/Tesoura
    Pedra ganha de Tesoura, Tesoura ganha de Papel, Papel ganha de Pedra
"""
import random

pontos_jog = 0
pontos_cpu = 0

opcoes = ['pedra', 'papel', 'tesoura']
rodadas = int( input('Quantas rodadas serão jogadas?: ') )

for i in range(rodadas):
    escolha_jog = ''
    while escolha_jog not in opcoes:
        escolha_jog = input('Digite a sua escolha ("pedra", "papel" ou "tesoura"): ')
        escolha_cpu = random.choice( opcoes )
        if escolha_jog not in opcoes:
            print('Informe uma opção válida.')
        elif escolha_jog == escolha_cpu:
            print('Deu empate!')
        elif (escolha_jog == 'pedra' and escolha_cpu == 'tesoura') \
            or (escolha_jog == 'papel' and escolha_cpu == 'pedra') \
            or (escolha_jog == 'tesoura' and escolha_cpu == 'papel'):
            pontos_jog += 1
            print('{} vs {}: Você ganhou do Computador!'.format(escolha_jog, escolha_cpu) )
        else:
            pontos_cpu += 1
            print('{} vs {}: O Computador ganhou de você!'.format(escolha_jog, escolha_cpu) )

print('Rodadas: {}, Jogador: {} ponto(s) / CPU: {} ponto(s)'.format(i+1, pontos_jog, pontos_cpu) )
if pontos_jog > pontos_cpu:
    print('Você ganhou do Computador')
elif pontos_jog < pontos_cpu:
    print('Você perdeu do Computador')
else:
    print('Não houve um vencedor.')

print('Fim da Disputa.')