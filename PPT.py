from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jog = int(input('Qual sua jogada? '))
print('-=' * 11)
print('Você jogou {}'.format(itens[jog]))
print('O computador escolheu {}'.format(itens[pc]))
print('-=' * 11)
if pc == 0:
    if jog == 0:
        print('Jogo Empatado!')
    elif jog ==1:
        print('Você Ganhou!!!')
    elif jog ==2:
        print('O Computador Ganhou!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 1:
    if jog == 0:
        print('O Computador Ganhou!!')
    elif jog == 1:
        print('Jogo Empatado!')
    elif jog == 2:
        print('Você Ganhou!!!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 2:
    if jog == 0:
        print('Você Ganhou!!!')
    elif jog ==1:
        print('O Computador Ganhou!')
    elif jog == 2:
        print('Jogo Empatado!')
    else:
        print('JOGADA INVÁLIDA!')
