import json

abrir = open('Quake.txt', 'r')  #leitura do arquivo de texto
totalKills = 0
lista = []
listaFinal = []
i= 1
final = {}

for linha in abrir:
    linha = linha.strip()  #remover espaços em brancos
    
    if linha.count("ClientUserinfoChanged"):  #armazenar nome do jogador numa variavel
    
        resultadoLinha = linha.split("\\")  #dividir a linha em indices pela \\
        nomeJogador = resultadoLinha[1]
        linha = linha.split(" ")  #dividir a linha em indices pelo espaço
        idJogador = linha[2]
        player = {}
        player['id'] = idJogador
        player['nome'] = nomeJogador
        player['kill'] = 0  
        player['nomeAntigo'] = ""
        if (len(lista)) == 0:
            lista.append(player)
           
        else:

            for elemento in lista:  #verificar se o nome já existe, depois inclui-lo
                
                if nomeJogador == elemento['nome']:
                    resultado = True
                    elemento['nome'] = player['nome']
                    break
                else:
                    resultado = False
                if player['id'] == elemento['id'] :  #substituir nome antigo
                    elemento['nomeAntigo'] = elemento['nome']
                    elemento['nome'] = player['nome']
                    resultado = True
                    break
            if resultado == False:
                lista.append(player)
    if linha.count("Kill"):  #fazer a contagem de kills
        totalKills +=1

        for elemento in lista:
            resultadoLinha = linha.split(" ")
            if elemento['id'] == resultadoLinha[2]:
               
                elemento['kill'] +=1

        if resultadoLinha[2] == "1022":  #contagem de kills do world
            elemento['kill'] -=1

    if linha.count("ShutdownGame"):  #encerrar game
        status = {}
        listaCopia = {}
        listaCopia = lista.copy()
                
        status['players'] = listaCopia

        status['game'] = i

        status['total kills'] = totalKills
        
        listaFinal.append(status)
        i +=1
        lista.clear()
        totalKills = 0

with open('listaFinal.json', 'w') as json_file:  #criar arquivo em json
    json.dump(listaFinal, json_file, indent=4)