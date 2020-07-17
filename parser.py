f = open('Quake.txt', 'r')
player = {}

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