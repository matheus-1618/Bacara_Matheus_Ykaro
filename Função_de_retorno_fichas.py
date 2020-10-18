def resultados(soma_cartas1,soma_cartas2):
        m=0
        i=0
        while m<j:
            while i<j:
                if escolhas[i]=='empate':
                    if soma_cartas1==soma_cartas2:
                        fichas[i]=fichas[i] +8*(emp[0])*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                        
                    else:
                        fichas[i]=fichas[i]- apostas[i]
                        print('Você perdeu,player {0}!'.format(i+1))
                        i+=1

                elif escolhas[i]=='banco':
                    if soma_cartas2>soma_cartas1:
                        fichas[i]=fichas[i] + (0.95)*(emp[1])*apostas[i]
                        print('Você ganhou,player {0}!'.format(i+1))
                        i+=1
                    else:
                        fichas[i]=fichas[i] -apostas[i]
                        print('Você perdeu, player {0}!'.format(i+1))
                        i+=1
                                    
                elif escolhas[i]=='jogador':
                    if soma_cartas1>soma_cartas2:
                        fichas[i]=fichas[i] +apostas[i]*(emp[2])
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
        m+=1  
        return fichas