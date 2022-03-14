"""Crie um programa que faça o computador jogar Jokenpô com você."""

from random import randint
from time import sleep
import emoji
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print(''' Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-='*11)
if computador == 0:  # computador jogou pedra
    if jogador == 0:
        print(emoji.emojize("\033[1;107;33m EMPATE :open_hands: \033[m", use_aliases=True))
    elif jogador == 1:
        print(emoji.emojize("\033[1;107;32m JOGADOR VENCEU :tada: \033[m", use_aliases=True))
    elif jogador == 2:
        print(emoji.emojize('\033[1;107;34m COMPUTADOR VENCEU :computer: \033[m', use_aliases=True))
    else:
        print(emoji.emojize('\033[1;107;31m JOGADA INVÁLIDA :no_entry_sign: \033[m', use_aliases=True))
if computador == 1:  # computador jogou papel
    if jogador == 0:
        print(emoji.emojize('\033[1;107;34m COMPUTADOR VENCEU :computer: \033[m', use_aliases=True))
    elif jogador == 1:
        print(emoji.emojize('\033[1;107;33m EMPATE :open_hands: \033[m', use_aliases=True))
    elif jogador == 2:
        print(emoji.emojize('\033[1;107;32m JOGADOR VENCEU :tada: \033[m', use_aliases=True))
    else:
        print(emoji.emojize('\033[1;107;31m JOGADA INVÁLIDA :no_entry_sign: \033[m', use_aliases=True))
if computador == 2:  # computador jogou tesoura
    if jogador == 0:
        print(emoji.emojize('\033[1;107;32m JOGADOR VENCEU :tada: \033[m', use_aliases=True))
    elif jogador == 1:
        print(emoji.emojize('\033[1;107;32m COMPUTADOR VENCEU :computer: \033[m', use_aliases=True))
    elif jogador == 2:
        print(emoji.emojize('\033[1;107;33m EMPATE  :open_hands: \033[m', use_aliases=True))
    else:
        print(emoji.emojize('\033[1;107;31m JOGADA INVÁLIDA  :no_entry_sign: \033[m', use_aliases=True))
