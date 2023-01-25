from random import randint
from time import sleep

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
jogadaPC = randint(0,2)

print(str('Suas opções:'))
print(str('''
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA
'''))
jogadaUser = int(input('Qual sua jogada: '))

print('JO')
sleep(.5)
print('KEN')
sleep(.5)
print('POOO!!!')

print('-=' * 13)
print('Computador jogou {}'.format(opcoes[jogadaPC]))
print('Voce jogou {}'.format(opcoes[jogadaUser]))
print('-=' * 13)


if jogadaPC == 0:
    if jogadaUser == 0:
        print('EMPATE')
    elif jogadaUser == 1:
        print('JOGADOR VENCEU!!')
    elif jogadaUser == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('Jogada Inválida!')
if jogadaPC == 1:
    if jogadaUser == 0:
        print('COMPUTADOR VENCEU!!')
    elif jogadaUser == 1:
        print('EMPATE')
    elif jogadaUser == 2:
        print('JOGADOR VENCEU!!')
    else:
        print('Jogada Inválida!')
if jogadaPC == 2:
    if jogadaUser == 0:
        print('JOGADOR VENCEU!!')
    elif jogadaUser == 1:
        print('COMPUTADOR VENCEU!!')
    elif jogadaUser == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida!')









