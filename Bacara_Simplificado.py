from math import floor
import random
print('''
Olá! Seja bem vindo ao Cassino Matheus&Ykaro! Iremos jogar Bacará Simplificado!
Nesta versão, não teremos a comissão da casa, multijogadores, multibaralhos, nem 
regras de distruibuição para terceira carta.
O jogo consiste em distribuir cartas de forma aleatória para o Banco e para o jogador.
Ganha quem chegar o mais próximo possível da soma 9.
''')
j=1
h=0
fichas=[]
while h<j:
    fichas1=float(input('Com quantas fichas você quer começar, player {0}: '.format(h+1)))
    fichas.append(fichas1)
    h+=1 
while True:
    a=False
    for m in fichas:
        if m==0 or m<1:
            print('Que pena, suas fichas acabaram, FIM DE JOGO!')
            a=True
    if a==True:
        break
    
    def resultados(soma_cartas1,soma_cartas2):
        m=0
        i=0
        while m<j:
            while i<j:
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*apostas[i]
                        fichas[i]=floor(fichas[i])
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                        
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        fichas[i]=floor(fichas[i])
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*apostas[i]
                        fichas[i]=floor(fichas[i])
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        fichas[i]=floor(fichas[i])
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1
                                    
                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]
                        fichas[i]=floor(fichas[i])
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1 
                    else:
                        fichas[i]=fichas[i] - apostas[i]
                        fichas[i]=floor(fichas[i])
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1
                else:
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=0
            m+=0
            return '''Recomeçando o jogo...'''
 
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
    c=False
    s=0
    while s<j:
        for m in fichas:
            print('Você tem {0} fichas, player {1}'.format(m,s+1))
            print('Em quem você deseja apostar? ')
            escolha1=input('''
            Banco('banco'),jogador('jogador') ou empate('empate')?
            Digite 'sair', para abandonar o jogo 
            ''')
            if escolha1=='sair' or escolha1=='Sair':
                c=True
                break
            else:
                escolhas.append(escolha1)
                s+=1
        s+=1
    
    if c==True:
        print(' Que pena que você desistiu')
        break

    f=0
    apostas=[]
    while f<j:
        aposta1=int(input('Quantas fichas você deseja apostar,player {0}: '.format(f+1)))
        apostas.append(aposta1)
        f+=1
    
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

    if soma_cartas1==8 or soma_cartas1==9:
        if soma_cartas2>9:
            soma_cartas2=soma_cartas2-10
            soma_cartas1=soma_cartas1
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
            
        elif soma_cartas2<=9:
            soma_cartas2=soma_cartas2
            soma_cartas1=soma_cartas1
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
              
    elif soma_cartas2==8 or soma_cartas2==9:
        if soma_cartas1>9:
            soma_cartas1=soma_cartas1-10
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
            
        elif soma_cartas1<=9:
            soma_cartas2=soma_cartas2
            soma_cartas1=soma_cartas1
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
            
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
                
            elif soma_cartas1>9 and soma_cartas2<=9:
                soma_cartas1=soma_cartas1-10
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                
            elif soma_cartas1<=9 and soma_cartas2>9:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2-10
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                 
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
                    x=resultados(soma_cartas1,soma_cartas2)
                    print(x)
                    
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
                    x=resultados(soma_cartas1,soma_cartas2)
                    print(x)
                     
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
                    x=resultados(soma_cartas1,soma_cartas2)
                    print(x)
            
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
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
        
        elif 6<=soma_cartas2<=7 and soma_cartas1<=5:
            g3=random.sample(numeros,1)
            g4=random.sample(naipes,1)
            print('A terceira carta do jogador é {0} do naipe {1}'.format(g3[0][0],g4[0]))
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2+ g3[0][1]
            if soma_cartas2>9:
                soma_cartas2-=10
            else:
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                
        elif 6<=soma_cartas1<=7 and 6<=soma_cartas2<=7:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
            
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
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                
            elif soma_cartas1>9 and soma_cartas2<=9:
                soma_cartas1=soma_cartas1-10
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                
            elif soma_cartas1<=9 and soma_cartas2>9:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2-10
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                  
            else:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                         
        elif soma_cartas1<=5 and 8<=soma_cartas1<=9:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
            
        elif 8<=soma_cartas1<=9 and soma_cartas2<=5:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
            
        elif soma_cartas1<=5 and 6<=soma_cartas2<=7:
            c2=random.sample(numeros,1)
            c3=random.sample(naipes,1)
            print('A terceira carta do jogador é {0} do naipe {1}'.format(c2[0][0],c3[0]))
            soma_cartas1+=c2[0][1]
            if soma_cartas1>9:
                soma_cartas1-=10
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                      
            else:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                        
        elif 6<=soma_cartas1<=7 and soma_cartas2<=5:
            d2=random.sample(numeros,1)
            d3=random.sample(naipes,1)
            print('A terceira carta do banco é {0} do naipe {1}'.format(d2[0][0],d3[0]))
            soma_cartas2+=d2[0][1]
            if soma_cartas2>9:
                soma_cartas2-=10
                soma_cartas1=soma_cartas1
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                
            else:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                
        else:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
            
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
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                    
            elif soma_cartas1>9 and soma_cartas2<=9:
                soma_cartas1-=9
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                
            elif soma_cartas1<=9 and soma_cartas2>9:
                soma_cartas1=soma_cartas1
                soma_cartas2-=10
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                
            else:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                
        elif soma_cartas1<=5 and 8<=soma_cartas1<=9:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
            
        elif 8<=soma_cartas1<=9 and soma_cartas2<=5:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
                
        elif soma_cartas1<=5 and 6<=soma_cartas2<=7:
            c2=random.sample(numeros,1)
            c3=random.sample(naipes,1)
            print('A terceira carta do jogador é {0} do naipe {1}'.format(c2[0][0],c3[0]))
            soma_cartas1+=c2[0][1]
            if soma_cartas1>9:
                soma_cartas1-=10
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                
            else:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                
        elif 6<=soma_cartas1<=7 and soma_cartas2<=5:
            d2=random.sample(numeros,1)
            d3=random.sample(naipes,1)
            print('A terceira carta do banco é {0} do naipe {1}'.format(d2[0][0],d3[0]))
            soma_cartas2+=d2[0][1]
            if soma_cartas2>9:
                soma_cartas2-=10
                soma_cartas1=soma_cartas1
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
                      
            else:
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)
                print(x)
           
        else:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
            
    elif 6<=soma_cartas1<=7 and soma_cartas2<=5:
        c1=random.sample(numeros,1)
        c2=random.sample(naipes,1)
        print('A terceira carta do banco é {0} do naipe {1}'.format(c1[0][0],c2[0]))
        soma_cartas2=soma_cartas2+c1[0][1]
        if soma_cartas2>9:
            soma_cartas2=soma_cartas2-10
            soma_cartas1=soma_cartas1
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
                  
        else:
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
                  
    elif 6<=soma_cartas2<=7 and soma_cartas1<=5:
        d1=random.sample(numeros,1)
        d2=random.sample(naipes,1)
        print('A terceira carta do jogador é {0} do naipe {1}'.format(d1[0][0],d2[0]))
        soma_cartas1=soma_cartas1+d1[0][1]
        if soma_cartas1>9:
            soma_cartas1=soma_cartas1-10
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
            
        else:
            soma_cartas2=soma_cartas2
            soma_cartas1=soma_cartas1
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
    
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
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
            
        elif soma_cartas1>9 and soma_cartas2<=9:
            soma_cartas1-=10
            soma_cartas1+=0
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
            
        elif soma_cartas1<=9 and soma_cartas2>9:
            soma_cartas1=soma_cartas1
            soma_cartas2-=10
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
        
        else:
            soma_cartas1+=0
            soma_cartas2+=0
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)    
    else:
        soma_cartas1=soma_cartas1
        soma_cartas2=soma_cartas2
        print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
        x=resultados(soma_cartas1,soma_cartas2)
        print(x)