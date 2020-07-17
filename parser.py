f = open('Quake.txt', 'r')
totalKills = 0
player = {}
lista = []
listaFinal = []
i= 1
for line in f:
    line = line.strip() #remover espaços em brancos
    
    if line.count("ClientUserinfoChanged"): #armazenar nome do jogador numa variavel
    
        line2 = line.split("\\")  #dividir a linha em indices pela \\
        nomeJogador = line2[1]
        line = line.split(" ") #dividir a linha em indices pelo espaõ
        idJogador = line[2]
        player = {}
        player['id'] = idJogador
        player['nome'] = nomeJogador
        player['kill'] = 0        
        if (len(lista)) == 0:
            lista.append(player)

        for elm in lista:
            
            if nomeJogador == elm['nome']:
                resultado = True
                elm['nome'] = player['nome']
                elm['id'] = idJogador
                break
            else:
                resultado = False
            if idJogador == elm['id']:
                elm['id'] = False

        if resultado == False:
            lista.append(player)
    if line.count("Kill"):
        totalKills +=1

        for elm in lista:
            line2 = line.split(" ")
            if elm['id'] == line2[2]:
               
                elm['kill'] +=1

        if line2[2] == "1022":
            elm['kill'] -=1

    if line.count("ShutdownGame"):
        
        listaFinal.append('game '+str(i))
        listaFinal.append('total Kills '+str(totalKills))
        listaFinal.extend(lista)
        i +=1
        lista.clear()
        totalKills = 0
               
                
for verLista in listaFinal:
    print(verLista)
