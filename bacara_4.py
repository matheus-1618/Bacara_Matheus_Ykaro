#EP  DESENVOLVIMENTO
import random
x=int(input('Quanto(s) player(s) você deseja no jogo? '))
o=int(input('Com quantos baralhos você(s) desejam jogar? 1, 6 ou 8? '))
fichas=[]
for i in range(0,x):
    fichas1=int(input('Com quantas fichas você quer começar, player {0}: '.format(i+1)))
    fichas.append(fichas1)

while True:#booleana 1
    if o==1 or o==6 or o==8:
        None
    else:
        print('Não temos essa opção de baralhos, recomece o jogo!')
    
    a=False
    for m in fichas:
        if m==0 or m<1:
            print('Que pena, as fichas de algum player, acabaram, FIM DE JOGO!')
            a=True
    
    if a==True: #condicional para a verdadeiro
        break
    
    às=['ás',1]
    dois=['dois',2]
    três=['três',3]
    quatro=['quatro',4]
    cinco=['cinco',5]
    seis=['seis',6]
    sete=['sete',7]
    oito=['oito',8]
    nove=['nove',9]
    dez=['dez',0]
    valete=['valete',0]
    dama=['dama',0]
    rei=['rei',0]
    
    escolhas=[]
    apostas=[]
    c=False
    i=0
    for m in fichas:
        print('Você tem {0} fichas, player {1}'.format(m,i+1))
        i+=1
        print('Em quem você deseja apostar? ')
        escolha1=input('''
        Banco('banco'),jogador('jogador') ou empate('empate')?
        Digite 'sair', para abandonar o jogo 
        ''')
        if escolha1=='sair' or escolha1=='Sair':
            c=True
        else:
            escolhas.append(escolha1)
    if c==True:
        print(' Que pena que você desistiu')
        break
    v=1
    for n in fichas:
        aposta1=float(input('Quantas fichas você deseja apostar,player {0}: '.format(v)))
        apostas.append(aposta1)
        v+=1
    

    b=0
    while b<len(escolhas):
        if escolhas[b]=='Sair' or escolhas[b]=='sair':
            print(' Que pena que você desistiu!Você saiu com {0:.2f} fichas'.format(float(fichas)))
            break
        else:
            b+=1

    

    numeros=[às,dois,três,quatro,cinco,seis,sete,oito,nove,dez,valete,dama,rei]*o
    naipes=['paus','ouros','espadas','copas']*o

    a=random.sample(numeros,1)
    b=random.sample(numeros,1)
    c=random.sample(numeros,1)
    d=random.sample(numeros,1)
    e=random.sample(naipes,1)
    f=random.sample(naipes,1)
    g=random.sample(naipes,1)
    h=random.sample(naipes,1)
    
    print(' As cartas do jogador são {0} do naipe {1} e {2} do naipe {3}'.format(a[0][0],e[0],b[0][0],f[0]))
    print(' As cartas do Banco são {0} do naipe {1} e {2} do naipe {3}'.format(c[0][0],g[0],d[0][0],h[0]))
    soma_cartas1= a[0][1]+b[0][1]
    soma_cartas2= c[0][1]+d[0][1]

    if soma_cartas1==8 or soma_cartas1==9:
        if soma_cartas2>9:
            soma_cartas2=soma_cartas2-10
            soma_cartas1=soma_cartas1
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                
        elif soma_cartas2<=9:
            soma_cartas2=soma_cartas2
            soma_cartas1=soma_cartas1
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
        
    elif soma_cartas2==8 or soma_cartas2==9:
        if soma_cartas1>9:
            soma_cartas1=soma_cartas1-10
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=1
        elif soma_cartas1<=9:
            soma_cartas2=soma_cartas2
            soma_cartas1=soma_cartas1
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=1
    elif soma_cartas1>9 and soma_cartas2>9:
        soma_cartas1=soma_cartas1-10
        soma_cartas2=soma_cartas2-10
        if soma_cartas1<=5 and soma_cartas2<=5:
            a1=random.sample(numeros,1)
            a2=random.sample(numeros,1)
            a3=random.sample(naipes,1)
            a4=random.sample(naipes,1)
            print('A terceira carta do jogador é {0} do naipe {1}'.format(a1[0][0],a3[0]))
            print('A terceira carta do banco é {0} do naipe {1}'.format(a2[0][0],a4[0]))
            soma_cartas1=soma_cartas1+a1[0][1]
            soma_cartas2=soma_cartas2+a2[0][1]
            if soma_cartas1>9 and soma_cartas2>9:
                soma_cartas1=soma_cartas1-10
                soma_cartas2=soma_cartas2-10
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1

                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
            elif soma_cartas1>9 and soma_cartas2<=9:
                soma_cartas1=soma_cartas1-10
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1

                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
            elif soma_cartas1<=9 and soma_cartas2>9:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2-10
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1

                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
            elif soma_cartas1<=9 and soma_cartas2<=9:
                if soma_cartas2<=5 and soma_cartas1<=5:
                    h1=random.sample(numeros,1)
                    h2=random.sample(numeros,1)
                    h3=random.sample(naipes,1)
                    h4=random.sample(naipes,1)
                    print('A terceira carta do jogador é {0} do naipe {1}'.format(h1[0][0],h3[0]))
                    print('A terceira carta do banco é {0} do naipe {1}'.format(h2[0][0],h4[0]))
                    soma_cartas1+=h1[0][1]
                    soma_cartas2+=h2[0][1]
                    print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                    i=0
                    while i<len(escolhas):
                        if escolhas[i]=='empate':
                            if soma_cartas1==soma_cartas2:
                                fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                                print('Você ganhou,player {0}!'.format(i+1))
                                i+=1
                            else:
                                fichas[i]=fichas[i]- apostas[i]
                                print('Você perdeu,player {0}!'.format(i+1))
                                i+=1

                        elif escolhas[i]=='banco':
                            if soma_cartas2>soma_cartas1:
                                fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                                print('Você ganhou,player {0}!'.format(i+1))
                                i+=1
                            else:
                                fichas[i]=fichas[i] -apostas[i]
                                print('Você perdeu, player {0}!'.format(i+1))
                                i+=1
                        elif escolhas[i]=='jogador':
                            if soma_cartas1>soma_cartas2:
                                fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                                print('Você ganhou, player {0}!'.format(i+1))
                                i+=1
                            else:
                                fichas[i]=fichas[i] - apostas[i]
                                print('Você perdeu, player {0}!'.format(i+1))
                                i+=1
                        else:
                            print('Parece que você digitou errado, recomece o jogo')
                            break
                        i+=1
                
                elif soma_cartas2<=5 and 6<=soma_cartas1<=7:
                    g1=random.sample(numeros,1)
                    g2=random.sample(naipes,1)
                    print('A terceira carta do jogador é {0} do naipe {1}'.format(g1[0][0],g2[0]))
                    soma_cartas2=soma_cartas2+g1[0][1]
                    soma_cartas1=soma_cartas1
                    if soma_cartas2>9:
                        soma_cartas2=soma_cartas2-10
                    else:
                        soma_cartas2=soma_cartas2
                    print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                    i=0
                    while i<len(escolhas):
                        if escolhas[i]=='empate':
                            if soma_cartas1==soma_cartas2:
                                fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                                print('Você ganhou,player {0}!'.format(i+1))
                                i+=1
                            else:
                                fichas[i]=fichas[i]- apostas[i]
                                print('Você perdeu,player {0}!'.format(i+1))
                                i+=1
                        elif escolhas[i]=='banco':
                            if soma_cartas2>soma_cartas1:
                                fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                                print('Você ganhou,player {0}!'.format(i+1))
                                i+=1
                            else:
                                fichas[i]=fichas[i] -apostas[i]
                                print('Você perdeu, player {0}!'.format(i+1))
                                i+=1
                        elif escolhas[i]=='jogador':
                            if soma_cartas1>soma_cartas2:
                                fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                                print('Você ganhou, player {0}!'.format(i+1))
                                i+=1
                            else:
                                fichas[i]=fichas[i] - apostas[i]
                                print('Você perdeu, player {0}!'.format(i+1))
                                i+=1

                        else:
                            print('Parece que você digitou errado, recomece o jogo')
                            break
                        i+=1
                elif soma_cartas1<=5 and 6<=soma_cartas2<=7:
                    f1=random.sample(numeros,1)
                    f2=random.sample(naipes,1)
                    print('A terceira carta do jogador é {0} do naipe {1}'.format(f1[0][0],f2[0]))
                    soma_cartas1=soma_cartas1+f1[0][1]
                    soma_cartas2=soma_cartas2
                    if soma_cartas1>9:
                        soma_cartas1=soma_cartas1-10
                    else:
                        soma_cartas1=soma_cartas1
                    print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                    i=0
                    while i<len(escolhas):
                        if escolhas[i]=='empate':
                            if soma_cartas1==soma_cartas2:
                                fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                                print('Você ganhou,player {0}!'.format(i+1))
                                i+=1
                            else:
                                fichas[i]=fichas[i]- apostas[i]
                                print('Você perdeu,player {0}!'.format(i+1))
                                i+=1

                        elif escolhas[i]=='banco':
                            if soma_cartas2>soma_cartas1:
                                fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                                print('Você ganhou,player {0}!'.format(i+1))
                                i+=1
                            else:
                                fichas[i]=fichas[i] -apostas[i]
                                print('Você perdeu, player {0}!'.format(i+1))
                                i+=1
                        elif escolhas[i]=='jogador':
                            if soma_cartas1>soma_cartas2:
                                fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                                print('Você ganhou, player {0}!'.format(i+1))
                                i+=1
                            else:
                                fichas[i]=fichas[i] - apostas[i]
                                print('Você perdeu, player {0}!'.format(i+1))
                                i+=1

                        else:
                            print('Parece que você digitou errado, recomece o jogo')
                            break
                        i+=1
        elif 6<=soma_cartas1<=7 and soma_cartas2<=5:
            f3=random.sample(numeros,1)
            f4=random.sample(naipes,1)
            print('A terceira carta do banco é {0} do naipe {1}'.format(f3[0][0],f4[0]))
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2+f3[0][1]
            if soma_cartas2>9:
                soma_cartas2-=10
            else:
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
            
        elif 6<=soma_cartas2<=7 and soma_cartas1<=5:
            g3=random.sample(numeros,1)
            g4=random.sample(naipes,1)
            print('A terceira carta do jogador é {0} do naipe {1}'.format(g3[0][0],g4[0]))
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2+g4[0][1]
            if soma_cartas2>9:
                soma_cartas2-=10
            else:
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
                
        elif 6<=soma_cartas1<=7 and 6<=soma_cartas2<=7:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
    
    elif soma_cartas1>9 and soma_cartas2<=9:
        soma_cartas1=soma_cartas1-10
        if soma_cartas1<=5 and soma_cartas2<=5:
            b1=random.sample(numeros,1)
            b2=random.sample(numeros,1)
            b3=random.sample(naipes,1)
            b4=random.sample(naipes,1)
            print('A terceira carta do jogador é {0} do naipe {1}'.format(b1[0][0],b3[0]))
            print('A terceira carta do banco é {0} do naipe {1}'.format(b2[0][0],b4[0]))
            soma_cartas1=soma_cartas1+b1[0][1]
            soma_cartas2=soma_cartas2+b2[0][1]
            if soma_cartas1>9 and soma_cartas2>9:
                soma_cartas1=soma_cartas1-10
                soma_cartas2=soma_cartas2-10
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
            elif soma_cartas1>9 and soma_cartas2<=9:
                soma_cartas1=soma_cartas1-10
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
            elif soma_cartas1<=9 and soma_cartas2>9:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2-10
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
            else:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
        elif soma_cartas1<=5 and 8<=soma_cartas1<=9:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
        elif 8<=soma_cartas1<=9 and soma_cartas2<=5:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
        elif soma_cartas1<=5 and 6<=soma_cartas2<=7:
            c2=random.sample(numeros,1)
            c3=random.sample(naipes,1)
            print('A terceira carta do jogador é {0} do naipe {1}'.format(c2[0][0],c3[0]))
            soma_cartas1+=c2[0][1]
            if soma_cartas1>9:
                soma_cartas1-=10
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
            else:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
        elif 6<=soma_cartas1<=7 and soma_cartas2<=5:
            d2=random.sample(numeros,1)
            d3=random.sample(naipes,1)
            print('A terceira carta do banco é {0} do naipe {1}'.format(d2[0][0],d3[0]))
            soma_cartas2+=d2[0][1]
            if soma_cartas2>9:
                soma_cartas2-=10
                soma_cartas1=soma_cartas1
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
            else:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
        else:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1
                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1
                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1
                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=1
    
    elif soma_cartas1<=9 and soma_cartas2>9:
        soma_cartas2=soma_cartas2-10
        if soma_cartas1<=5 and soma_cartas2<=5:
            d1=random.sample(numeros,1)
            d2=random.sample(numeros,1)
            d3=random.sample(naipes,1)
            d4=random.sample(naipes,1)
            print('A terceira carta do jogador é {0} do naipe {1}'.format(d1[0][0],d3[0]))
            print('A terceira carta do banco é {0} do naipe {1}'.format(d2[0][0],d4[0]))
            soma_cartas1+=d1[0][1]
            soma_cartas2+=d2[0][1]
            if soma_cartas1>9 and soma_cartas2>9:
                soma_cartas1-=10
                soma_cartas2-=10
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                        i+=1
            elif soma_cartas1>9 and soma_cartas2<=9:
                soma_cartas1-=9
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1

                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
            elif soma_cartas1<=9 and soma_cartas2>9:
                soma_cartas1=soma_cartas1
                soma_cartas2-=10
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1

                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
            else:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1

        elif soma_cartas1<=5 and 8<=soma_cartas1<=9:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=1
        elif 8<=soma_cartas1<=9 and soma_cartas2<=5:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=1
        elif soma_cartas1<=5 and 6<=soma_cartas2<=7:
            c2=random.sample(numeros,1)
            c3=random.sample(naipes,1)
            print('A terceira carta do jogador é {0} do naipe {1}'.format(c2[0][0],c3[0]))
            soma_cartas1+=c2[0][1]
            if soma_cartas1>9:
                soma_cartas1-=10
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1

                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
            else:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1
                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
        elif 6<=soma_cartas1<=7 and soma_cartas2<=5:
            d2=random.sample(numeros,1)
            d3=random.sample(naipes,1)
            print('A terceira carta do banco é {0} do naipe {1}'.format(d2[0][0],d3[0]))
            soma_cartas2+=d2[0][1]
            if soma_cartas2>9:
                soma_cartas2-=10
                soma_cartas1=soma_cartas1
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1

                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
            else:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                i=0
                while i<len(escolhas):
                    if escolhas[i]=='empate':
                        if soma_cartas1==soma_cartas2:
                            fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i]- apostas[i]
                            print('Você perdeu,player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='banco':
                        if soma_cartas2>soma_cartas1:
                            fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                            print('Você ganhou,player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] -apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1

                    elif escolhas[i]=='jogador':
                        if soma_cartas1>soma_cartas2:
                            fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                            print('Você ganhou, player {0}!'.format(i+1))
                            i+=1
                        else:
                            fichas[i]=fichas[i] - apostas[i]
                            print('Você perdeu, player {0}!'.format(i+1))
                            i+=1

                    else:
                        print('Parece que você digitou errado, recomece o jogo')
                        break
                    i+=1
        else:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=1
    
    elif 6<=soma_cartas1<=7 and soma_cartas2<=5:
        c1=random.sample(numeros,1)
        c2=random.sample(naipes,1)
        print('A terceira carta do banco é {0} do naipe{1}'.format(c1[0][0],c2[0]))
        soma_cartas2=soma_cartas2+c1[0][1]
        if soma_cartas2>9:
            soma_cartas2=soma_cartas2-10
            soma_cartas1=soma_cartas1
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=1
        else:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=1
    elif 6<=soma_cartas2<=7 and soma_cartas1<=5:
        d1=random.sample(numeros,1)
        d2=random.sample(naipes,1)
        print('A terceira carta do jogador é {0} do naipe {1}'.format(d1[0][0],d2[0]))
        soma_cartas1=soma_cartas1+d1[0][1]
        if soma_cartas1>9:
            soma_cartas1=soma_cartas1-10
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=1
        else:
            soma_cartas2=soma_cartas2
            soma_cartas1=soma_cartas1
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=1
    elif  soma_cartas1<=5 and soma_cartas2<=5:
        a2=random.sample(numeros,1)
        b2=random.sample(numeros,1)
        c2=random.sample(naipes,1)
        d2=random.sample(naipes,1)
        print('A terceira carta do jogador é {0} do naipe {1}'.format(a2[0][0],c2[0]))
        print('A terceira carta do banco é {0} do naipe {1}'.format(b2[0][0],d2[0]))
        soma_cartas1=soma_cartas1+a2[0][1]
        soma_cartas2=soma_cartas2+b2[0][1]
        if soma_cartas1>9 and soma_cartas2>9:
            soma_cartas1-=10
            soma_cartas2-=10
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=1
        elif soma_cartas1>9 and soma_cartas2<=9:
            soma_cartas1-=10
            soma_cartas1+=0
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=1
        elif soma_cartas1<=9 and soma_cartas2>9:
            soma_cartas1=soma_cartas1
            soma_cartas2-=10
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=1
        else:
            soma_cartas1+=0
            soma_cartas2+=0
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            i=0
            while i<len(escolhas):
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1
                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=1
    else:
        soma_cartas1=soma_cartas1
        soma_cartas2=soma_cartas2
        print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
        i=0
        while i<len(escolhas):
            if escolhas[i]=='empate':
                if soma_cartas1==soma_cartas2:
                    fichas[i]=fichas[i] +8*(1-0.1436)*apostas[i]
                    print('Você ganhou,player {0}!'.format(i+1))
                    i+=1
                else:
                    fichas[i]=fichas[i]- apostas[i]
                    print('Você perdeu,player {0}!'.format(i+1))
                    i+=1

            elif escolhas[i]=='banco':
                if soma_cartas2>soma_cartas1:
                    fichas[i]=fichas[i] + (0.95)*(1-0.0106)*apostas[i]
                    print('Você ganhou,player {0}!'.format(i+1))
                    i+=1
                else:
                    fichas[i]=fichas[i] -apostas[i]
                    print('Você perdeu, player {0}!'.format(i+1))
                    i+=1

            elif escolhas[i]=='jogador':
                if soma_cartas1>soma_cartas2:
                    fichas[i]=fichas[i] +apostas[i]*(1-0.024)
                    print('Você ganhou, player {0}!'.format(i+1))
                    i+=1
                else:
                    fichas[i]=fichas[i] - apostas[i]
                    print('Você perdeu, player {0}!'.format(i+1))
                    i+=1

            else:
                print('Parece que você digitou errado, recomece o jogo')
                break
            i+=1

    
    
