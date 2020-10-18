#EP-Design de Software
#Equipe: Matheus Silva Melo de Oliveira e Ykaro Andrade
#Data: 18/10/2020
from math import floor #Importando função que arredondará a quantidade de fichas para baixo, evitando possibilidade de fichas centesimais.
import random #Importando módulo que disponibilizará a função "sample", que irá sortear aleatoriamente as cartas utilizadas  no jogo. 
print('''
Olá! Seja bem vindo ao Cassino Matheus&Ykaro! Iremos jogar Bacará!
Nesta versão temos várias medidas implementadas, que simulam uma boa experiência de jogo.
O jogo consiste em distribuir cartas de forma aleatória para o Banco e para o jogador.
Caso queira descobrir mais sobre as regras, leia no arquivo READ ME, disposto no github.
Ganha quem chegar o mais próximo possível da soma 9.
''') #Painel de início do jogo
j=int(input('Quanto(s) player(s) você deseja no jogo? ')) #Entrada de dados respectiva a quantidade de players a apostarem
o=int(input('Com quantos baralhos você(s) deseja(m) jogar? 1, 6 ou 8? ')) #Entrada de dados respectiva a quantidade de baralhos escolhidos, e suas taxas respectivas

h=0
fichas=[] #lista vazia que irá receber a quantidade de fichas compradas/escolhidas por cada player ao iniciar o jogo, de acordo com seu índice
while h<j: #Loop com intuito de registrar a quantidade inicial de fichas adquiridas por cada player no balcão do cassino para o jogo
    fichas1=float(input('Com quantas fichas você quer começar, player {0}: ?'.format(h+1)))#Quantidade de fichas compradas por cada player
    fichas.append(fichas1) #Armazenamento da quantidade de fichas
    h+=1

while True: #Loop verdadeiro que, fora uma quantidade de fichas igual a zero ou necessidade de saída de algum player, continua a rodar o jogo.
    if o==1: #Escolha de jogo com um baralho
        emp=[1-0.1575,1-0.0101,1-0.0129]#Taxas para um baralho. Taxas na seguinte ordem: Empate, Banco e Jogador.
        
    elif o==6:#Escolha de jogo com seis baralhos
        emp=[1-0.1444,1-0.0106,1-0.0124]#Taxas para seis baralhos. Taxas na seguinte ordem: Empate, Banco e Jogador.
    
    elif o==8:#Escolha de jogo com oito baralhos
        emp=[1-0.1436,1-0.0106,1-0.0124]#Taxas para um baralho. Taxas na seguinte ordem: Empate, Banco e Jogador.
    
    else: #condicional para o caso em que o player informa um número de baralho não permitido
        print('Não temos essa opção de baralhos, recomece o jogo!')
        break

    a=False #Definindo booleana para encerrar o jogo em caso de falta de fichas de algum player
    for m in fichas: #Loop para a verificação de alguma quantidade nula de fichas no lista que armazena esses valores
        if m==0 or m<1: #condicional para averiguação do caso acima
            print('Que pena, as fichas de algum player, acabaram, FIM DE JOGO!')
            a=True #Mudança da booleana 
    if a==True: #Condicional para, em caso de alternação da booleana, iniciar o processo de finalização do jogo.
        break #Finalização do jogo
    
    def resultados(soma_cartas1,soma_cartas2):#Função que estabelece, de acordo com as somas das cartas, o retorno das apostas de cada player
        m=0
        i=0
        while m<j:
            while i<j:
                if escolhas[i]=='empate':#Condicional para player que apostou no empate
                    if soma_cartas1==soma_cartas2: #Soma do banco similar a do jogador
                        fichas[i]=fichas[i] +8*(emp[0])*apostas[i]#retorno das fichas, com correção da taxa especificada pela quantidade de baralhos escolhidos
                        fichas[i]=floor(fichas[i])#Função de arredondamento das fichas
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                        
                    else:
                        fichas[i]=fichas[i]- apostas[i]#retorno das fichas
                        fichas[i]=floor(fichas[i])#Função de arredondamento das fichas
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':#Condicional para player que apostou no banco
                    if soma_cartas2>soma_cartas1: #soma do banco mais próxima de nove que a do jogador
                        fichas[i]=fichas[i] + (0.95)*(emp[1])*apostas[i]#retorno das fichas, com correção da taxa especificada pela quantidade de baralhos escolhida
                        fichas[i]=floor(fichas[i])#Função de arredondamento das fichas
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]#Retorno das fichas
                        fichas[i]=floor(fichas[i])#Arredondamento das fichas
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1
                                    
                elif escolhas[i]=='jogador':#Condicional para player que apostou no jogador
                    if soma_cartas1>soma_cartas2: #soma do jogador mais próxima de nove que a do banco
                        fichas[i]=fichas[i] +apostas[i]*(emp[2])#Retorno de fichas com correção especificada pela quantidade de baralhos escolhida
                        fichas[i]=floor(fichas[i])#Arredondamento das fichas
                        print('Você ganhou, player {0}!'.format(i+1))
                        i+=1 
                    else:
                        fichas[i]=fichas[i] - apostas[i]#Retorno das fichas
                        fichas[i]=floor(fichas[i])#Arredondamento das fichas
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1
                else:#Condição caso o player digite qualquer coisa diferente de banco,jogador,empate ou sair.
                    print('Parece que você digitou errado, recomece o jogo')
                    break
                i+=0
            m+=0
            return '''Recomeçando o jogo...'''#Retorno da função para reinício do jogo
    
    #definição de listas refentes aos valores de cada carta do baralho, recebendo sua string de nomeação de carta e seu respectivo valor para a soma.           
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
        
    escolhas=[] #Lista que armazenará a escolha de aposta de cada player, refereciando ao seu índice
    c=False #Booleana que, caso alterne para True, iniciará o processo de desistência de um player.
    s=0
    while s<j:#Loop de adição progressiva dos dados a lista 'escolhas'
        for m in fichas: #Loop com objetivo de manter a escolha individual quando há dois ou mais players
            print('Você tem {0} fichas, player {1}'.format(m,s+1)) #Informação das fichas em estoque disponíveis para aposta
            print('Em quem você deseja apostar? ')
            escolha1=input('''
            Banco('banco'),jogador('jogador') ou empate('empate')?
            Digite 'sair', para abandonar o jogo 
            ''') #Entrada de dados respectivos a escolha de qual ponto(empate,jogador ou banco) o player irá apostar
            if escolha1=='sair' or escolha1=='Sair': #Condicional de contemplação para players desistentes
                c=True #Alternação da booleana
            else: # Entrada de dados respectivos a escolha, caso for digitado algo diferente das possibilidades do input, a função 'soma_cartas' avisará o erro de digitação.
                escolhas.append(escolha1) #adição dos dados a lista de armazenamento de cada escolha
                s+=1
        s+=1
    if c==True: #Processo de desistência de player desistente
        print(' Que pena que você desistiu')
        break
    
    f=0
    apostas=[] #Lista de armazenamento do valor apostado de cada player
    while f<j: #Loop para receber o valor da aposta em cada rodada, por player respectivo 
        aposta1=float(input('Quantas fichas você deseja apostar,player {0}: '.format(f+1)))#Entrada da aposta de cada player, em seu indice
        apostas.append(aposta1)#Adição dos dados de aposta na lista
        f+=1
        
    numeros=[às,dois,três,quatro,cinco,seis,sete,oito,nove,dez,valete,dama,rei]*o #Lista que guarda a carta especificada do baralho, e sua quantidade, escolhida pelo player.
    naipes=['paus','ouros','espadas','copas']*o #Naipe da carta escolhida anteriormente, também sujeita a quantidade de baralhos escolhidas
    #Função que realizará ,de forma aleatória, o sorteio das 2 cartas iniciais do jogador e do banco.
    a=random.sample(numeros,1)
    b=random.sample(numeros,1)
    c=random.sample(numeros,1)
    d=random.sample(numeros,1)
    e=random.sample(naipes,1)
    f=random.sample(naipes,1)
    g=random.sample(naipes,1)
    h=random.sample(naipes,1)
        
    print(' As cartas do jogador são {0} do naipe {1} e {2} do naipe {3}'.format(a[0][0],e[0],b[0][0],f[0])) #Saída de dados, informando as cartas iniciais do jogador
    print(' As cartas do Banco são {0} do naipe {1} e {2} do naipe {3}'.format(c[0][0],g[0],d[0][0],h[0])) #Saída de dados, informando as cartas iniciais do banco
    soma_cartas1= a[0][1]+b[0][1] #Variável que armazenará o valor inicial da soma do jogador
    soma_cartas2= c[0][1]+d[0][1] #Variável que armazenará o valor incial da soma do banco

    if soma_cartas1==8 or soma_cartas1==9: #condicional para quando a soma de cartas do jogador é 8 ou 9, não resultando na terceira carta do banco, mesmo abaixo de 5 
        if soma_cartas2>9: #se a soma de cartas do banco for maior que 9, considera-se somente a unidade
            soma_cartas2=soma_cartas2-10 # Atualização do valor da soma do banco
            soma_cartas1=soma_cartas1
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2) #Utilização da função para retorno das fichas
            print(x)
                 
        elif soma_cartas2<=9: #Em caso contrrário, a soma continua a mesma
            soma_cartas2=soma_cartas2
            soma_cartas1=soma_cartas1
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
            
        
    elif soma_cartas2==8 or soma_cartas2==9: #condicional para quando a soma de cartas do banco é 8 ou 9, não resultando na terceira carta do jogador, mesmo com soma abaixo de 5 
        if soma_cartas1>9: #se a soma de cartas do jogador for maior que 9,  considera-se somente a unidade
            soma_cartas1=soma_cartas1-10
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
            
            
        elif soma_cartas1<=9: #Em caso contrário, a soma é mantida a mesma.
            soma_cartas2=soma_cartas2
            soma_cartas1=soma_cartas1
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
            
    elif soma_cartas1>9 and soma_cartas2>9: #para o caso em que a soma de cartas do jogador e do banco são maiores que 9, considera-se apenas a unidade em ambos
        soma_cartas1=soma_cartas1-10
        soma_cartas2=soma_cartas2-10
        if soma_cartas1<=5 and soma_cartas2<=5: #se a nova soma de cartas do jogador e do banco forem menores ou iguais a 5, é sorteada uma terceira carta para ambos
            a1=random.sample(numeros,1)
            a2=random.sample(numeros,1)
            a3=random.sample(naipes,1)
            a4=random.sample(naipes,1)
            print('A terceira carta do jogador é {0} do naipe {1}'.format(a1[0][0],a3[0]))# Saída de dados informando a nova carta do jogador
            print('A terceira carta do banco é {0} do naipe {1}'.format(a2[0][0],a4[0]))# Saída de dados informando a nova carta do banco
            soma_cartas1=soma_cartas1+a1[0][1]#Atualização da soma do jogador
            soma_cartas2=soma_cartas2+a2[0][1]#Atualização da soma do banco
            if soma_cartas1>9 and soma_cartas2>9: #se a soma de cartas tanto do jogador quanto do banco forem maiores do que 9, considera-se novamente a unidade
                soma_cartas1=soma_cartas1-10
                soma_cartas2=soma_cartas2-10
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                
            elif soma_cartas1>9 and soma_cartas2<=9: #quando a soma do jogador é maior que nove, considera-se a unidade, enquanto o banco não sofre mudanças na soma
                soma_cartas1=soma_cartas1-10
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                
                
            elif soma_cartas1<=9 and soma_cartas2>9: #quando a soma do banco é maior que nove, considera-se somente a unidade, enquanto o jogador não sofre mudanças na soma
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2-10
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                   
            elif soma_cartas1<=9 and soma_cartas2<=9: #condicional para quando a soma do jogador e do banco são menores ou iguais a 9, gerando uma série de casos
                if soma_cartas2<=5 and soma_cartas1<=5: #Caso em que ambas as somas, são menores ou iguais a cinco, gerando a terceira carta para ambos
                    h1=random.sample(numeros,1)
                    h2=random.sample(numeros,1)
                    h3=random.sample(naipes,1)
                    h4=random.sample(naipes,1)
                    print('A terceira carta do jogador é {0} do naipe {1}'.format(h1[0][0],h3[0]))#Saída de dados da terceira carta do jogador
                    print('A terceira carta do banco é {0} do naipe {1}'.format(h2[0][0],h4[0]))#Saída de dados da terceira carta do banco
                    soma_cartas1+=h1[0][1]#Atualização da soma do jogador
                    soma_cartas2+=h2[0][1]#Atualização da soma do banco
                    print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                    x=resultados(soma_cartas1,soma_cartas2)
                    print(x)
                    
                elif soma_cartas2<=5 and 6<=soma_cartas1<=7: #caso a soma de cartas do banco for igual ou menor a 5 e a soma do jogador for igual a 6 ou 7, é sorteado uma terceira carta apenas para o banco 
                    g1=random.sample(numeros,1)
                    g2=random.sample(naipes,1)
                    print('A terceira carta do jogador é {0} do naipe {1}'.format(g1[0][0],g2[0]))
                    soma_cartas2=soma_cartas2+g1[0][1] #atualização da soma do banco
                    soma_cartas1=soma_cartas1
                    if soma_cartas2>9: #se a soma de cartas do banco for maior que 9, considera-se somente a unidade
                        soma_cartas2=soma_cartas2-10
                    else: #Caso contrário, a soma não muda
                        soma_cartas2=soma_cartas2
                    print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                    x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                    print(x)
                    
                elif soma_cartas1<=5 and 6<=soma_cartas2<=7: #Caso a soma do banco seja 6 ou 7 e a soma do jogador inferior ou igual a 5, este último recebe a terceira carta
                    f1=random.sample(numeros,1)
                    f2=random.sample(naipes,1)
                    print('A terceira carta do jogador é {0} do naipe {1}'.format(f1[0][0],f2[0]))#Saída de dados informando a terceira do jogador
                    soma_cartas1=soma_cartas1+f1[0][1]#Atualização do valor da soma do jogador
                    soma_cartas2=soma_cartas2
                    if soma_cartas1>9: #se a soma de cartas do jogador for maior que 9, considera-se a unidade
                        soma_cartas1=soma_cartas1-10
                    else: #se não, a soma permanece igual
                        soma_cartas1=soma_cartas1
                    print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                    x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                    print(x)
            
        elif 6<=soma_cartas1<=7 and soma_cartas2<=5: #Caso a soma do jogador seja 6 ou 7, e do banco acima ou igual a 5, somente o último recebe a terceira carta
            f3=random.sample(numeros,1)
            f4=random.sample(naipes,1)
            print('A terceira carta do banco é {0} do naipe {1}'.format(f3[0][0],f4[0]))#Saída de dados para informar a terceira carta do banco
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2+f3[0][1]
            if soma_cartas2>9: #se a soma de cartas do banco for maior que 9, considera-se somente a unidade
                soma_cartas2-=10
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
            else: #se não, a soma permanece igual
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
           
        elif 6<=soma_cartas2<=7 and soma_cartas1<=5:  #Caso a soma do banco seja 6 ou 7, e do jogador acima ou igual a 5, somente o último recebe a terceira carta
            g3=random.sample(numeros,1)
            g4=random.sample(naipes,1)
            print('A terceira carta do jogador é {0} do naipe {1}'.format(g3[0][0],g4[0]))#Saída de dados para informar a nova carta do jogador
            soma_cartas2=soma_cartas2
            soma_cartas1=soma_cartas1+ g3[0][1]#atualização da soma do jogador
            if soma_cartas2>9: #se a soma de cartas do banco for maior que 9, considera-se a unidade
                soma_cartas2-=10
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
            else: #se não, a soma permanece igual
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                
        elif 6<=soma_cartas1<=7 and 6<=soma_cartas2<=7: #condicional para o caso em que a soma de cartas do jogador e a soma do banco são iguais a 6 e/ou iguais a 7, a soma permanece a mesma para ambos
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)
            print(x)
            
    elif soma_cartas1>9 and soma_cartas2<=9: #Caso a soma do jogador seja maior que 9 (considera-se a unidade), e a do banco menor que 9(sujeita a casos)
        soma_cartas1=soma_cartas1-10
        if soma_cartas1<=5 and soma_cartas2<=5: #condicional para o caso em que tanto a soma de cartas do jogador quanto a do banco são menores e/ou iguais a 5, é sorteada uma carta para cada um
            b1=random.sample(numeros,1)
            b2=random.sample(numeros,1)
            b3=random.sample(naipes,1)
            b4=random.sample(naipes,1)
            print('A terceira carta do jogador é {0} do naipe {1}'.format(b1[0][0],b3[0]))#Saída de dados para nova carta do jogador
            print('A terceira carta do banco é {0} do naipe {1}'.format(b2[0][0],b4[0]))#Saída de dados para nova carta do banco
            soma_cartas1=soma_cartas1+b1[0][1]#Atualização da soma do jogador
            soma_cartas2=soma_cartas2+b2[0][1]#Atualização da soma do banco
            if soma_cartas1>9 and soma_cartas2>9: #condicional para o caso em que tanto a soma de cartas do jogador quanto a do banco são maiores que 9, considera-se somente a unidade
                soma_cartas1=soma_cartas1-10
                soma_cartas2=soma_cartas2-10
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                
            elif soma_cartas1>9 and soma_cartas2<=9: #Caso a soma do jogador seja maior que 9, considera-se somente a unidade, e a do banco seja inferior a nove, sujeita a casos
                soma_cartas1=soma_cartas1-10
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                
            elif soma_cartas1<=9 and soma_cartas2>9: #Caso a soma do banco seja maior que 9, considera-se somente a unidade, e a do jogador seja inferior a nove, sujeita a casos
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2-10
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                
                
            else: #se não, a soma permanece igual para ambos
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                
                
        elif soma_cartas1<=5 and 8<=soma_cartas1<=9: #Caso a soma do jogador seja 8 ou 9,  não é sorteada uma terceira carta para o banco.
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
            
        elif 8<=soma_cartas1<=9 and soma_cartas2<=5: #Caso a soma do banco seja 8 ou 9,  não é sorteada uma terceira carta para o jogador.
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
            
        elif soma_cartas1<=5 and 6<=soma_cartas2<=7:#Caso a soma do jogador seja menor ou igual a 5 e a do banco 6 ou 7, é sorteada uma terceira carta para o jogador
            c2=random.sample(numeros,1)
            c3=random.sample(naipes,1)
            print('A terceira carta do jogador é {0} do naipe {1}'.format(c2[0][0],c3[0]))#Saída de dados para informar a terceira carta do jogador
            soma_cartas1+=c2[0][1]#Atualização da soma do jogador
            if soma_cartas1>9:#Se a soma do jogador seja maior que nove, considera-se a unidade
                soma_cartas1-=10
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                      
            else:# Caso contrário, a soma permanece inalterada
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                        
        elif 6<=soma_cartas1<=7 and soma_cartas2<=5:#Caso a soma do banco seja menor ou igual a 5 e a do banco 6 ou 7, é sorteada uma terceira carta para o banco
            d2=random.sample(numeros,1)
            d3=random.sample(naipes,1)
            print('A terceira carta do banco é {0} do naipe {1}'.format(d2[0][0],d3[0]))#Saída de dados para informar a terceira carta do banco
            soma_cartas2+=d2[0][1]#Atualização da soma do banco
            if soma_cartas2>9:#Caso a soma do banco seja maior qu 9, considera-se a unidade
                soma_cartas2-=10
                soma_cartas1=soma_cartas1
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                
            else:#Caso contrário, a soma permanece inalterada
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                
        else:#Casos adversos, a soma se mantém constante
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
            
    elif soma_cartas1<=9 and soma_cartas2>9:#Caso a soma do banco seja maior que nove, considera-se a unidade, e a do jogador menor que 9, é sujeita a casos
        soma_cartas2=soma_cartas2-10
        if soma_cartas1<=5 and soma_cartas2<=5:#Caso ambas as somas sejam inferiores ou iguais a 5, ambos recebem a terceira carta
            d1=random.sample(numeros,1)
            d2=random.sample(numeros,1)
            d3=random.sample(naipes,1)
            d4=random.sample(naipes,1)
            print('A terceira carta do jogador é {0} do naipe {1}'.format(d1[0][0],d3[0]))#Saída de dados para informar a terceira carta do jogador
            print('A terceira carta do banco é {0} do naipe {1}'.format(d2[0][0],d4[0]))#Saída de dados para informar a terceira carta do banco
            soma_cartas1+=d1[0][1]#Atualização da soma do jogador
            soma_cartas2+=d2[0][1]#Atualização da soma do banco
            if soma_cartas1>9 and soma_cartas2>9:#Caso ambas as somas sejam maiores que 9, considera-se somente a unidade
                soma_cartas1-=10
                soma_cartas2-=10
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                    
            elif soma_cartas1>9 and soma_cartas2<=9:#Caso a soma do jogador seja maior que 9, considera-se somente a unidade
                soma_cartas1-=10
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                
            elif soma_cartas1<=9 and soma_cartas2>9:#Caso a soma do banco seja maior que 9, considera-se somente a unidade
                soma_cartas1=soma_cartas1
                soma_cartas2-=10
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                
            else:#Casos adjacentes, a soma continua constante
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                
        elif soma_cartas1<=5 and 8<=soma_cartas1<=9:#Caso a soma do jogador seja inferior ou igual a 5, e do banco igual a 8 ou 9, o primeiro não recebe terceira carta
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
            
        elif 8<=soma_cartas1<=9 and soma_cartas2<=5:#Caso a soma do banco seja inferior ou igual a 5, e do jogador igual a 8 ou 9, o primeiro não recebe terceira carta
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
                
        elif soma_cartas1<=5 and 6<=soma_cartas2<=7:#Caso a soma do jogador seja inferior ou igual a 5, e a do banco igual a 6 ou 7, o primeiro recebe a terceira carta
            c2=random.sample(numeros,1)
            c3=random.sample(naipes,1)
            print('A terceira carta do jogador é {0} do naipe {1}'.format(c2[0][0],c3[0]))#Saída de dados para informar a terceira carta do jogador
            soma_cartas1+=c2[0][1]#Atualização do valor da soma do jogador
            if soma_cartas1>9:#Caso a soma seja maior que 9, considera-se a unidade
                soma_cartas1-=10
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                
            else:#Caso contrário, a soma se mantém constante
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                
        elif 6<=soma_cartas1<=7 and soma_cartas2<=5:#Caso a soma do jogador seja igual a 6 ou 7, e a do banco menor ou igual a 5, o último recebe a terceira carta
            d2=random.sample(numeros,1)
            d3=random.sample(naipes,1)
            print('A terceira carta do banco é {0} do naipe {1}'.format(d2[0][0],d3[0]))#Saída de dados informando a terceira carta do banco
            soma_cartas2+=d2[0][1]#Atualização da soma do banco
            if soma_cartas2>9:#Caso a soma do banco seja maior que 9, considera-se a unidade
                soma_cartas2-=10
                soma_cartas1=soma_cartas1
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
                      
            else:#Casos adjacentes, a soma permanece inalterada
                soma_cartas1=soma_cartas1
                soma_cartas2=soma_cartas2
                print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
                x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
                print(x)
           
        else:#Casos suplementares, a soma se mantém inalterada
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
            
    elif 6<=soma_cartas1<=7 and soma_cartas2<=5:#Caso  a soma do jogador seja 6 ou 7 e a do banco menor ou igual a 5, o último recebe a terceira carta
        c1=random.sample(numeros,1)
        c2=random.sample(naipes,1)
        print('A terceira carta do banco é {0} do naipe{1}'.format(c1[0][0],c2[0]))#Saída de dados para informar a terceira carta do banco
        soma_cartas2=soma_cartas2+c1[0][1]#Atualização da soma do banco
        if soma_cartas2>9:#Caso a soma do banco ultrapasse 9, considera-se a unidade
            soma_cartas2=soma_cartas2-10
            soma_cartas1=soma_cartas1
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
                  
        else:#Quaisquer outros casos, a soma permanece a mesma
            soma_cartas1=soma_cartas1
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
                  
    elif 6<=soma_cartas2<=7 and soma_cartas1<=5:#Caso a soma do banco seja 6 ou 7 e a do jogador esteja abaixo ou igual a 5, o último recebe a terceira carta
        d1=random.sample(numeros,1)
        d2=random.sample(naipes,1)
        print('A terceira carta do jogador é {0} do naipe {1}'.format(d1[0][0],d2[0]))#Saída de dados para informar a terceira carta do jogador
        soma_cartas1=soma_cartas1+d1[0][1]#Atualização da soma do jogador
        if soma_cartas1>9:#Caso a soma do jogador seja maior que 9, considera-se a unidade
            soma_cartas1=soma_cartas1-10
            soma_cartas2=soma_cartas2
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
            
        else:#Casos adjacentes, a soma permanece a mesma
            soma_cartas2=soma_cartas2
            soma_cartas1=soma_cartas1
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
    
    elif  soma_cartas1<=5 and soma_cartas2<=5:#Caso ambos jogador e banco tenham somas inferiores a 5, ambos recebem a terceira carta
        a2=random.sample(numeros,1)
        b2=random.sample(numeros,1)
        c2=random.sample(naipes,1)
        d2=random.sample(naipes,1)
        print('A terceira carta do jogador é {0} do naipe {1}'.format(a2[0][0],c2[0]))#Saída de dados para informar a terceira carta do jogador
        print('A terceira carta do banco é {0} do naipe {1}'.format(b2[0][0],d2[0]))#Saída de dados para informar a terceira carta do banco
        soma_cartas1=soma_cartas1+a2[0][1]#Atualização da soma do jogador
        soma_cartas2=soma_cartas2+b2[0][1]#Atualização da soma do banco
        if soma_cartas1>9 and soma_cartas2>9:#Caso ambas as somas sejam superiores a 9, considera-se a unidade
            soma_cartas1-=10
            soma_cartas2-=10
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
            
        elif soma_cartas1>9 and soma_cartas2<=9:#Caso somente a soma do jogador seja superior a 9, considera-se a unidade
            soma_cartas1-=10
            soma_cartas1+=0
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
            
        elif soma_cartas1<=9 and soma_cartas2>9:#Caso somente a soma do banco seja superior a 9, considera-se somente a unidade
            soma_cartas1=soma_cartas1
            soma_cartas2-=10
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
        
        else:#Casos adjacentes, a soma permanece constante
            soma_cartas1+=0
            soma_cartas2+=0
            print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
            x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
            print(x)
            
    else:#Casos adjacentes a soma permanece constante
        soma_cartas1=soma_cartas1
        soma_cartas2=soma_cartas2
        print('A soma do jogador é {0} e do banco é {1}'.format(soma_cartas1,soma_cartas2))
        x=resultados(soma_cartas1,soma_cartas2)#Utilização da função para retorno das fichas
        print(x)
