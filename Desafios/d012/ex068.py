import random

jogador = computador = escolhajogador = escolhacomputador = contador = 0
#1 é Par / 2 é Ímpar

while True:
    escolhajogador = int(input('Você quer par ou ímpar? 1(Par) ou 2(Ímpar) '))
    if escolhajogador == 1:
        escolhacomputador = 2
    elif escolhajogador == 2:
        escolhacomputador = 1
    else:
        print('Você digitou errado, tente novamente!')
    print('A escolha do computador é Par' if escolhacomputador == 1 else 'A escolha do computador é Ímpar')
    print('A escolha do jogador é Par' if escolhajogador == 1 else 'A escolha do jogador é Ímpar')

    computador = random.randint(1, 5)
    print(f'A jogada do computador é {computador}')
    jogador = int(input('Qual a sua jogada? '))
    print(f'A minha jogada é {jogador}')

    if (jogador % 2 == 0 and computador % 2 == 0) or (jogador % 2 == 1 and computador % 2 == 1):
        if escolhajogador == 1:
            contador += 1
            print(f'Parabéns! Você ganhou! E já tem {contador} vitórias.')
        if escolhajogador == 2:
            print('Que pena, você perdeu!')
            break
    if (jogador % 2 == 1 and computador % 2 == 0) or (jogador % 2 == 0 and computador % 2 == 1):
        if escolhajogador == 2:
            contador += 1
            print(f'Parabéns! Você ganhou! E já tem {contador} vitórias.')
        if escolhajogador == 1:
            print('Que pena, você perdeu!')
            break






