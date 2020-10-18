import random

print('''
Bem vindo ao Cassino MathYkaro!
Somos especializados no jogo de Bacará, seja com 
um, seis ou oito baralhos!
O valor de cada carta é estabelecidoda seguinte forma:
às=1
dois=2
três=3
quatro=4
cinco=5
seis=6
sete=7
oito=8
nove=9
dez=0
valete=0
dama=0
rei=0
Decida sua aposta, você começa com 100 fichas!
''')
fichas=100
while True:
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
    escolha=input('Em quem você deseja apostar? Banco,jogador ou empate? ')
    aposta=int(input('Quantas fichas você deseja apostar: '))
    numeros=[às,dois,três,quatro,cinco,seis,sete,oito,nove,dez,valete,dama,rei]
    naipes=['paus','ouros','espadas','copas']
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
    soma_jogador=soma_cartas1
    soma_banco=soma_cartas2
    if soma_cartas1 <= 5 or soma_cartas2 <= 5:
        i=random.sample(numeros,1)
        j=random.sample(naipes,1)
        print('A terceira carta do jogador é {0} do naipe {1}'.format(i[0][0],j[0]))
        soma_cartas1=a[0][1]+b[0][1]+i[0][1]
        if soma_cartas1<=9 :
            soma_jogador=soma_cartas1
            print(' A soma do jogador é {0}'.format(soma_jogador))
            print('A soma do Banco é {0}'.format(soma_banco))
        elif 10 <= soma_cartas1 <=19 :
            soma_jogador= soma_cartas1 - 10
            print(' A soma do jogador é {0}'.format(soma_jogador))
            print('A soma do Banco é {0}'.format(soma_banco))
        elif 20 <= soma_cartas1 <= 27:
            soma_jogador= soma_cartas1 -20
            print(' A soma do jogador é {0}'.format(soma_jogador))
            print('A soma do Banco é {0}'.format(soma_banco))
    if soma_cartas2 <= 5:
        k=random.sample(numeros,1)
        l=random.sample(naipes,1)
        print('A terceira carta do banco é {0} do naipe {1}'.format(k[0][0],l[0]))
        print('A soma do Banco é {0}'.format(soma_banco))
        soma_cartas2=c[0][1]+d[0][1]+k[0][1]
        if soma_cartas2<=9:
            soma_banco=soma_cartas2
            print(' A soma do jogador é {0}'.format(soma_jogador))
            print('A soma do Banco é {0}'.format(soma_banco))
        elif 10 <= soma_cartas2 <=19:
            soma_banco= soma_cartas2 - 10
            print(' A soma do jogador é {0}'.format(soma_jogador))
            print('A soma do Banco é {0}'.format(soma_banco))
        elif 20 <= soma_cartas2 <= 27:
            soma_banco= soma_cartas2 -20
            print(' A soma do jogador é {0}'.format(soma_jogador))
            print('A soma do Banco é {0}'.format(soma_banco))
    elif 8<= soma_cartas1 <=9 or 8<=soma_cartas2<=9:
        soma_cartas1=soma_jogador
        soma_cartas2=soma_banco
        print(' A soma do jogador é {0}'.format(soma_jogador))
        print('A soma do Banco é {0}'.format(soma_banco))
    elif 19>=soma_cartas1>9 or 19>=soma_cartas2>9:
        soma_jogador=soma_cartas1-10
        soma_banco=soma_cartas2-10
        print(' A soma do jogador é {0}'.format(soma_jogador))
        print('A soma do Banco é {0}'.format(soma_banco))
    elif 27>=soma_cartas1>19 or 27>=soma_cartas2>19:
        soma_jogador=soma_cartas1-20
        soma_banco=soma_cartas2-20
        print(' A soma do jogador é {0}'.format(soma_jogador))
        print('A soma do Banco é {0}'.format(soma_banco))
    elif 6<=soma_cartas1<=7:
        soma_cartas1=soma_jogador
        print(' A soma do jogador é {0}'.format(soma_jogador))
        print('A soma do Banco é {0}'.format(soma_banco))
    elif 6<=soma_cartas2<=7:
        soma_cartas2=soma_banco
        print(' A soma do jogador é {0}'.format(soma_jogador))
        print('A soma do Banco é {0}'.format(soma_banco))

    print(' A soma do jogador é {0}'.format(soma_jogador))
    print('A soma do Banco é {0}'.format(soma_banco))   
