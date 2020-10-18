x=int(input('Quantos players você deseja no jogo? '))

fichas=[]
for i in range(0,x):
    fichas1=int(input('Com quantas fichas você quer começar, player {0}: '.format(i+1)))
    fichas.append(fichas1)

escolhas=[]
apostas=[]
i=0
for m in escolhas:
    print('Você tem {0} fichas, player {1}'.format(m,i+1))
    i+=1
    print('Em quem você deseja apostar? ')
    escolha1=input('''
    Banco('banco'),jogador('jogador') ou empate('empate')?
    Digite 'sair', para abandonar o jogo 
    ''')
    escolhas.append(escolha1)
    aposta1=float(input('Quantas fichas você deseja apostar: '))
    apostas.append(aposta1)

i=0
while i<len(escolhas):
    if escolhas[i]=='empate':
        if soma_cartas1==soma_cartas2:
            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
            print('Você ganhou,player {0}!'.format(i+1))
        else:
            fichas[i]=fichas[i]- apostas[i]
            print('Você perdeu,player {0}!'.format(i+1))

    elif escolha1=='banco':
        if soma_cartas2>soma_cartas1:
            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
            print('Você ganhou,player {0}!'.format(i+1))
        else:
            fichas[i]=fichas[i] -apostas[i]
            print('Você perdeu, player {0}!'.format(i+1))

    elif escolha1=='jogador':
        if soma_cartas1>soma_cartas2:
            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
            print('Você ganhou, player {0}!'.format(i+1))
        else:
            fichas[i]=fichas[i] - apostas[i]
            print('Você perdeu, jogador {0}!'.format(i+1))

    else:
        print('Parece que você digitou errado, recomece o jogo')
        break
print(escolhas)
print(apostas)
