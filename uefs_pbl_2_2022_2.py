'''Jogo das somas 2.0'''
#Autor: Diogo dos Santos de Jesus
#Componente Curricular: Algoritmos I
#Concluído em: 13/11/2022
#Declaro que este código foi elaborado por mim de forma individual e não contém
#nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
#código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

import random

def fazmatriz(nivel):
    '''função que cria e retorna uma matriz 4x4 ou 9x9 de zeros dependendo do paramêtro nível'''
    if nivel == "1":
        indice_oculta = 5
    elif nivel == "2":
        indice_oculta = 10
    matriz = []
    for i in range(indice_oculta):
        linha = []
        for j in range(indice_oculta):
            linha.append(0)
        matriz.append(linha)
    return matriz

def fucmatriz_oculta(matriz, nivel):
    '''função que cria e retorna a matriz oculta que pode ser 9x9 ou 4x4 depedendo do paramêtro'''
    if nivel == "1":
        indice_oculta = 5
    elif nivel == "2":
        indice_oculta = 10
    matriz_oculta_funcao = []
    for i in range(indice_oculta):
        linha = []
        for j in range(indice_oculta):
            linha.append("○")
        matriz_oculta_funcao.append(linha)
    for i in range(indice_oculta-1): # Esse loop atribui as somas da linhas à matriz oculta, ficando como ultimo elemento de cada linha da matriz
        matriz_oculta_funcao[i][indice_oculta-1] = matriz[i][indice_oculta-1]
    for j in range(indice_oculta-1): # Esse loop atribui as somas da colunas à matriz oculta, ficando como ultimo elemento de cada coluna da matriz
        matriz_oculta_funcao[indice_oculta-1][j] = matriz[indice_oculta-1][j]

    return matriz_oculta_funcao

def encontrarnumero(matriz, secao, numero, nivel):
    '''funcao que encontra o numero na seção.'''
    if nivel == "1":
        if secao == 1:
            loopi, loopif = 0, 2
            loopj, loopfj = 0, 2
        elif secao == 4:
            loopi, loopif = 2, 4
            loopj, loopfj = 2, 4
        elif secao == 2:
            loopi, loopif = 0, 2
            loopj, loopfj = 2, 4
        elif secao == 3:
            loopi, loopif = 2, 4
            loopj, loopfj = 0, 2
    elif nivel == "2":
        if secao == 1:
            loopi, loopif = 0, 3
            loopj, loopfj = 0, 3
        elif secao == 2:
            loopi, loopif = 0, 3
            loopj, loopfj = 3, 6
        elif secao == 3:
            loopi, loopif = 0, 3
            loopj, loopfj = 6, 9
        elif secao == 4:
            loopi, loopif = 3, 6
            loopj, loopfj = 0, 3
        elif secao == 5:
            loopi, loopif = 3, 6
            loopj, loopfj = 3, 6
        elif secao == 6:
            loopi, loopif = 3, 6
            loopj, loopfj = 6, 9
        elif secao == 7:
            loopi, loopif = 6, 9
            loopj, loopfj = 0, 3
        elif secao == 8:
            loopi, loopif = 6, 9
            loopj, loopfj = 3, 6
        elif secao == 9:
            loopi, loopif = 6, 9
            loopj, loopfj = 6, 9
    for i in range(loopi, loopif): # Aqui o loop vai rodar dependendo de qual seção foi escolhida.
        for j in range(loopj, loopfj):
            if matriz[i][j] == numero: # Se ele achar o número que o usuário digitou
                if matriz[i][j] != matrizoculta[i][j]: # Se o número já não foi escolhido, retorna a posição.
                    return (i, j)
                else: # Caso ele já tenha sido escolhido, retorna falso.
                    return False

def mostrarmatriz(matriz, nivel):
    '''Printa uma matriz 4x4 ou 9x9 depedendo do parametro.'''
    if nivel == "1":
        indice = 5
        print('╔'+'═'*(len(matriz) * 2) + '╦' + '═'*(len(matriz) * 2) + '╗') # Teto da matriz
        for linha in range(indice):
            for coluna in range(indice):
                if coluna % 2 == 0:
                    print("║", end = "") # Caso o número seja o ultimo antes de ir para a seção do lado ele printa um divisor de seção.
                print(f'{matriz[linha][coluna]:^5}', end = "")
            if (linha+1) % 2 == 0: # Caso seja a última linha antes de ir pra terceira e quarta seção ele printa esses divisores.
                print()
                for x in range(2):
                    print("╬"+ "═"*10, end = "")
                print("╬", end = "")
            print()
    elif nivel == "2":
        indice = 10
        print('╔'+'═'*(15) + '╦' + '═'*(15) + '╦'+'═'*(15)+ '╗') # Teto da matriz
        for linha in range(indice):
            for coluna in range(indice):
                if coluna % 3 == 0:
                    print("║", end = "") # Mesma lógica da nivel 1, só muda índice.
                print(f'{matriz[linha][coluna]:^5}', end = "")
            if (linha+1) % 3 == 0: # Mesma lógica da nivel 1, só muda índice.
                print()
                for x in range(3):
                    print("╬"+ "═"*15, end = "")
                print("╬", end = "")
            print()

def somarlinhas(matriz, nivel):
    '''função que soma as linhas de uma matriz'''
    if nivel == "1":
        indice = 4
    else:
        indice = 9
    # Loop que itera sob os valores de uma linha, soma os valores da linha na variavel acumuladora e coloca esse valor como ultimo elemento da linha na matriz.
    for linhas in range(indice):
        linha_soma = 0 # Variavel utilizada para acumular a soma da linha.
        for colunas in range(indice):
            linha_soma += matriz[linhas][colunas]
        matriz[linhas][indice] = linha_soma
    return matriz

def somardiagonal(matriz, nivel):
    '''Soma a diagonal da matriz'''
    if nivel == "1":
        indice = 4
    else:
        indice = 9
    # Mesma lógica da função de somarlinhas
    diagonal_soma = 0
    for diagonal in range(indice):
        diagonal_soma += matriz[diagonal][diagonal]
    matriz[indice][indice] = diagonal_soma

    return matriz

def somarcolunas(matriz, nivel):
    '''função que soma as colunas de uma matriz'''
    if nivel == "1":
        indice = 4
    else:
        indice = 9
    # Mesma lógica da função de somarlinhas
    for colunas in range(indice):
        coluna_soma = 0
        for linhas in range(indice):
            coluna_soma += matriz[linhas][colunas]
        matriz[indice][colunas] = coluna_soma

    return matriz

def randomizar(matriz_random, nivel):
    '''função que randomiza o tabuleiro'''
    if nivel == "1":
        for x in range(4):
            if x == 0:
                loopi, loopif = 0, 2
                loopj, loopfj = 0, 2
            elif x == 1:
                loopi, loopif = 2, 4
                loopj, loopfj = 2, 4
            elif x == 2:
                loopi, loopif = 0, 2
                loopj, loopfj = 2, 4
            elif x == 3:
                loopi, loopif = 2, 4
                loopj, loopfj = 0, 2
            k = 0 # Váriavel que vai ser utilizada para índice da lista.
            numeros_secao = [1,2,3,4] # Lista usada para definir os números da seção
            random.shuffle(numeros_secao) # Embaralha a lista.
            for i in range(loopi, loopif): # Os dois loop vão percorrer e randomizar cada seção depedendo do valor de x, sendo este para linhas e o debaixo, para colunas
                for j in range(loopj, loopfj):
                    matriz_random[i][j] = numeros_secao[k] # O número da posição [i][j] vai ser o número de indice k da lista de numeros_secao
                    k += 1 # Soma +1 para pegar o próximo número da lista de numero da seção.
    elif nivel == "2": # Mesma lógica do nível 1.
        for x in range(9):
            if x == 0:
                loopi, loopif = 0, 3
                loopj, loopfj = 0, 3
            elif x == 1:
                loopi, loopif = 0, 3
                loopj, loopfj = 3, 6
            elif x == 2:
                loopi, loopif = 0, 3
                loopj, loopfj = 6, 9
            elif x == 3:
                loopi, loopif = 3, 6
                loopj, loopfj = 0, 3
            elif x == 4:
                loopi, loopif = 3, 6
                loopj, loopfj = 3, 6
            elif x == 5:
                loopi, loopif = 3, 6
                loopj, loopfj = 6, 9
            elif x == 6:
                loopi, loopif = 6, 9
                loopj, loopfj = 0, 3
            elif x == 7:
                loopi, loopif = 6, 9
                loopj, loopfj = 3, 6
            elif x == 8:
                loopi, loopif = 6, 9
                loopj, loopfj = 6, 9
            k = 0
            numeros_secao = [1,2,3,4,5,6,7,8,9]
            random.shuffle(numeros_secao)
            for i in range(loopi, loopif):
                for j in range(loopj, loopfj):
                    matriz_random[i][j] = numeros_secao[k]
                    k += 1

    return somardiagonal(somarcolunas(somarlinhas(matriz_random, nivel), nivel), nivel)

def divisores():
    '''função que cria divisores de menu'''
    print('═'*50)

def checar_linha(matriz_oculta, nivel):
    '''Checa se uma linha já foi preenchida de numeros'''
    if nivel == "1":
        loopfim = 4
    else:
        loopfim = 9
    linha1 = True
    linha2 = True
    linha3 = True
    linha4 = True
    linha5 = True
    linha6 = True
    linha7 = True
    linha8 = True
    linha9 = True
    for j in range(loopfim): # Loop que roda as linhas, caso o nível seja 1, vai apenas de 0 à 3, caso seja 2, vai de 0, 9
        if isinstance(matriz_oculta[0][j], str) is True: # Checa se na linha da matriz oculta ainda há strings, ou seja se ainda não foi totalmente descoberta.
            linha1 = False # Caso a linha não esteja preenchida, a variável é trocada para falsa e quando é falsa, não vai ser considerada para somar na função de soma de pontos.
        if isinstance(matriz_oculta[1][j], str) is True: # Mesma lógica para as próximas linhas.
            linha2 = False
        if isinstance(matriz_oculta[2][j], str) is True:
            linha3 = False
        if isinstance(matriz_oculta[3][j], str) is True:
            linha4 = False
        if nivel == "2":
            if isinstance(matriz_oculta[4][j], str) is True:
                linha5 = False
            if isinstance(matriz_oculta[5][j], str) is True:
                linha6 = False
            if isinstance(matriz_oculta[6][j], str) is True:
                linha7 = False
            if isinstance(matriz_oculta[7][j], str) is True:
                linha8 = False
            if isinstance(matriz_oculta[8][j], str) is True:
                linha9 = False
    if nivel == "1":
        return (linha1, linha2, linha3, linha4)
    else:
        return (linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9)

def checar_coluna(matriz_oculta, nivel):
    '''Checa se uma coluna já foi preenchida de numeros'''
    coluna_1 = True
    coluna_2 = True
    coluna_3 = True
    coluna_4 = True
    coluna_5 = True
    coluna_6 = True
    coluna_7 = True
    coluna_8 = True
    coluna_9 = True
    if nivel == "1":
        loopfim = 4
    else:
        loopfim = 9
    for i in range(loopfim): # Mesma lógica utiliza na checagem de linhas.
        if isinstance(matriz_oculta[i][0], str) is True:
            coluna_1 = False
        if isinstance(matriz_oculta[i][1], str) is True:
            coluna_2 = False
        if isinstance(matriz_oculta[i][2], str) is True:
            coluna_3 = False
        if isinstance(matriz_oculta[i][3], str) is True:
            coluna_4 = False
        if nivel == "2":
            if isinstance(matriz_oculta[i][4], str) is True:
                coluna_5 = False
            if isinstance(matriz_oculta[i][5], str) is True:
                coluna_6 = False
            if isinstance(matriz_oculta[i][6], str) is True:
                coluna_7 = False
            if isinstance(matriz_oculta[i][7], str) is True:
                coluna_8 = False
            if isinstance(matriz_oculta[i][8], str) is True:
                coluna_9 = False
    if nivel == "1":
        return (coluna_1, coluna_2, coluna_3, coluna_4)
    else:
        return (coluna_1, coluna_2, coluna_3, coluna_4, coluna_5, coluna_6, coluna_7, coluna_8, coluna_9)

def checar_diagonal(matriz_oculta, nivel):
    '''Checa se a diagonal principal já foi encontrada'''
    if nivel == "1":
        loopfim = 4
    else:
        loopfim = 9
    diagonal = True
    for i in range(loopfim): # Mesma lógica da checagem de linha e coluna.
        if isinstance(matriz_oculta[i][i], str) is True:
            diagonal = False
    return diagonal

def somar_pontos(linhas, colunas, diagonal, nivel):
    '''Atribui os pontos ao jogador'''
    if nivel == "1":
        pontos = 0 # Variavel acumuladora para somar os pontos.
        linha_1, linha_2, linha_3, linha_4 = linhas # Vem da checagem de linha
        coluna_1, coluna_2, coluna_3, coluna_4 = colunas # Vem da checagem de linha
        diagonal_principal = diagonal # Vem da checagem de linha
        if linha_1 is True: # Se a linha não há mais strings ela pode ser somada.
            if isinstance(matrizjogo[0][4], str) is False: # Caso o elemento que contém a soma de pontos da linha não é string.
                pontos += matrizjogo[0][4] # Os pontos são somados para a váriavel acumuladora de pontos.
            matrizjogo[0][4] = str(matrizjogo[0][4]) # O elemento que contém a soma de pontos da linha, vira string, logo ele fica desconsiderado para próximas somas.
        if linha_2 is True: # Mesma lógica da linha 1, será aplicada para essas e para próximas linhas, colunas e diagonal.
            if isinstance(matrizjogo[1][4], str) is False:
                pontos += matrizjogo[1][4]
            matrizjogo[1][4] = str(matrizjogo[1][4])
        if linha_3 is True:
            if isinstance(matrizjogo[2][4], str) is False:
                pontos += matrizjogo[2][4]
            matrizjogo[2][4] = str(matrizjogo[2][4])
        if linha_4 is True:
            if isinstance(matrizjogo[3][4], str) is False:
                pontos += matrizjogo[3][4]
            matrizjogo[3][4] = str(matrizjogo[3][4])
        if coluna_1 is True:
            if isinstance(matrizjogo[4][0], str) is False:
                pontos += matrizjogo[4][0]
            matrizjogo[4][0] = str(matrizjogo[4][0])
        if coluna_2 is True:
            if isinstance(matrizjogo[4][1], str) is False:
                pontos += matrizjogo[4][1]
            matrizjogo[4][1] = str(matrizjogo[4][1])
        if coluna_3 is True:
            if isinstance(matrizjogo[4][2], str) is False:
                pontos += matrizjogo[4][2]
            matrizjogo[4][2] = str(matrizjogo[4][2])
        if coluna_4 is True:
            if isinstance(matrizjogo[4][3], str) is False:
                pontos += matrizjogo[4][3]
            matrizjogo[4][3] = str(matrizjogo[4][3])
        if diagonal_principal is True:
            if isinstance(matrizjogo[4][4], str) is False:
                pontos += (matrizjogo[4][4]) * 2
            matrizjogo[4][4] = str(matrizjogo[4][4])
            matrizoculta[4][4] = matrizjogo[4][4]
        return pontos # Retorna os pontos para o jogador da rodada.

    elif nivel == "2": # Mesma lógica da nivel 1.
        pontos = 0
        linha_1, linha_2, linha_3, linha_4, linha_5, linha_6, linha_7, linha_8, linha_9 = linhas # Mesma lógica da nivel 1.
        coluna_1, coluna_2, coluna_3, coluna_4, coluna_5, coluna_6, coluna_7, coluna_8, coluna_9 = colunas # Mesma lógica da nivel 1.
        diagonal_principal = diagonal # Mesma lógica da nivel 1.
        if linha_1 is True: # Mesma lógica da nivel 1.
            if isinstance(matrizjogo[0][9], str) is False:
                pontos += matrizjogo[0][9]
            matrizjogo[0][9] = str(matrizjogo[0][9])
        if linha_2 is True:
            if isinstance(matrizjogo[1][9], str) is False:
                pontos += matrizjogo[1][9]
            matrizjogo[1][9] = str(matrizjogo[1][9])
        if linha_3 is True:
            if isinstance(matrizjogo[2][9], str) is False:
                pontos += matrizjogo[2][9]
            matrizjogo[2][9] = str(matrizjogo[2][9])
        if linha_4 is True:
            if isinstance(matrizjogo[3][9], str) is False:
                pontos += matrizjogo[3][9]
            matrizjogo[3][9] = str(matrizjogo[3][9])
        if linha_5 is True:
            if isinstance(matrizjogo[4][9], str) is False:
                pontos += matrizjogo[4][9]
            matrizjogo[4][9] = str(matrizjogo[4][9])
        if linha_6 is True:
            if isinstance(matrizjogo[5][9], str) is False:
                pontos += matrizjogo[5][9]
            matrizjogo[5][9] = str(matrizjogo[5][9])
        if linha_7 is True:
            if isinstance(matrizjogo[6][9], str) is False:
                pontos += matrizjogo[6][9]
            matrizjogo[6][9] = str(matrizjogo[6][9])
        if linha_8 is True:
            if isinstance(matrizjogo[7][9], str) is False:
                pontos += matrizjogo[7][9]
            matrizjogo[7][9] = str(matrizjogo[7][9])
        if linha_9 is True:
            if isinstance(matrizjogo[8][9], str) is False:
                pontos += matrizjogo[8][9]
            matrizjogo[8][9] = str(matrizjogo[8][9])
        if coluna_1 is True:
            if isinstance(matrizjogo[9][0], str) is False:
                pontos += matrizjogo[9][0]
            matrizjogo[9][0] = str(matrizjogo[9][0])
        if coluna_2 is True:
            if isinstance(matrizjogo[9][1], str) is False:
                pontos += matrizjogo[9][1]
            matrizjogo[9][1] = str(matrizjogo[9][1])
        if coluna_3 is True:
            if isinstance(matrizjogo[9][2], str) is False:
                pontos += matrizjogo[9][2]
            matrizjogo[9][2] = str(matrizjogo[9][2])
        if coluna_4 is True:
            if isinstance(matrizjogo[9][3], str) is False:
                pontos += matrizjogo[9][3]
            matrizjogo[9][3] = str(matrizjogo[9][3])
        if coluna_5 is True:
            if isinstance(matrizjogo[9][4], str) is False:
                pontos += matrizjogo[9][4]
            matrizjogo[9][4] = str(matrizjogo[9][4])
        if coluna_6 is True:
            if isinstance(matrizjogo[9][5], str) is False:
                pontos += matrizjogo[9][5]
            matrizjogo[9][5] = str(matrizjogo[9][5])
        if coluna_7 is True:
            if isinstance(matrizjogo[9][6], str) is False:
                pontos += matrizjogo[9][6]
            matrizjogo[9][6] = str(matrizjogo[9][6])
        if coluna_8 is True:
            if isinstance(matrizjogo[9][7], str) is False:
                pontos += matrizjogo[9][7]
            matrizjogo[9][7] = str(matrizjogo[9][7])
        if coluna_9 is True:
            if isinstance(matrizjogo[9][8], str) is False:
                pontos += matrizjogo[9][8]
            matrizjogo[9][8] = str(matrizjogo[9][8])
        if diagonal_principal is True:
            if isinstance(matrizjogo[9][9], str) is False:
                pontos += (matrizjogo[9][9]) * 2
            matrizjogo[9][9] = str(matrizjogo[9][9])
            matrizoculta[9][9] = matrizjogo[9][9]
        return pontos # Retorna os pontos para o jogador da rodada.

def definir_vencedor(matriz_oculta, jogador_um, jogador_dois, nivel):
    '''Define o vencedor do jogo.'''
    if jogador_um > jogador_dois:
        vencedor = "jogador 1"
    elif jogador_dois > jogador_um:
        vencedor = "jogador 2"
    else:
        vencedor = "O jogo deu empate"
    for checador in checar_coluna(matriz_oculta, nivel): # Testa os returns da checagem de coluna.
        if not checador: # Caso ele ache uma váriavel falsa, ou seja, ainda tem coluna para ser preenchida.
            return False
    return vencedor # Retorna o vencedor do jogo.

def checar_numero(numero, tamanhomatriz):
    '''Checa se o numero da seção está no range válido.'''
    if tamanhomatriz == "1":
        if not 1 <= int(numero) <= 4:
            return False
        else:
            return True
    elif tamanhomatriz == "2":
        if not 1 <= int(numero) <= 9:
            return False
        else:
            return True

def escolha_dificuldade():
    '''Função onde é solicitada ao usuário a escolha da dificuldade.'''
    dificuldade_correta = True # Utilizada para fazer o loop da escolha de dificuldade.
    while dificuldade_correta:
        divisores()
        print("Escolha o nível do tabuleiro: \n1) Nível 1 (4x4) \n2) Nível 2 (9x9)")
        divisores()
        dificuldadef = input("Escolha: ")
        divisores()
        if dificuldadef == "1":
            matrizjogof = randomizar(fazmatriz(dificuldadef), dificuldadef) # Chama as função de fazer matriz e randomizar.
            matrizocultaf = fucmatriz_oculta(matrizjogof, dificuldadef) # Faz a matriz oculta a partir da matriz de jogo.
            dificuldade_correta = False
        elif dificuldadef == "2":
            matrizjogof = randomizar(fazmatriz(dificuldadef), dificuldadef) # Mesma lógica para dificuldade 1.
            matrizocultaf = fucmatriz_oculta(matrizjogof, dificuldadef) # Mesma lógica para dificuldade 1.
            dificuldade_correta = False
        else:
            print("Dificuldade inválida.")
    return matrizjogof, matrizocultaf, dificuldadef # Retorna a matriz com os resultados, a matriz com os números ocultos e a dificuldade.

def main():
    '''Principal programa, onde o usuário joga.'''
    jogador1 = 0 # Variável utilizada para guardar os pontos do jogador1
    jogador2 = 0 #Variável utilizada para guardar os pontos do jogador2
    rodada = 0 #Usada para fazer a alternancia de jogada entre os jogadores
    loop = True # Usada para fazer o loop principal do jogo
    while loop:
        encontrou = True # Váriavel para utilizar como laço de repetição.
        mostrarmatriz(matrizoculta, dificuldade) # Mostra a matriz para que o usuário jogue.
        divisores()
        if rodada == 0:
            print("Agora é a vez do jogador 1")
        else:
            print("Agora é a vez do jogador 2")
        divisores()
        while encontrou:
            secao_input = input("Escolha uma seção: ")
            divisores()
            while not secao_input.isnumeric() or checar_numero(secao_input, dificuldade) is False: # Enquanto a seção não seja um número de 1 até 4(matriz4x4) ou 9 (matriz9x9), isso vai repetir.
                print("Número inválido")
                divisores()
                secao_input = input("Escolha uma seção: ")
            numero_secao = input("Escolha um número: ")
            divisores()
            while not numero_secao.isnumeric() or checar_numero(numero_secao, dificuldade) is False: # Mesma lógica da seção.
                print("Número inválido.")
                divisores()
                numero_secao = input("Escolha um número: ")
                divisores()
            divisores()
            if (encontrarnumero(matrizjogo, int(secao_input), int(numero_secao), dificuldade)) is not False: # Aqui é checado se o número foi escolhido ou não
                posicao_linha, posicao_coluna = encontrarnumero(matrizjogo, int(secao_input), int(numero_secao), dificuldade) # Caso não tenha sido escolhido
                encontrou = False
            else: # Se o número digitado já foi escolhido.
                print("Este número já foi escolhido.")
                divisores()
        matrizoculta[posicao_linha][posicao_coluna] = matrizjogo[posicao_linha][posicao_coluna] # Depois da checagem, o número entra na matrizoculta
        if rodada == 0: # Alternancia de rodada, quando a rodada é 0 o jogador1 ganha os pontos caso complete uma linha/coluna/diagonal
            jogador1 += somar_pontos(checar_linha(matrizoculta, dificuldade), checar_coluna(matrizoculta, dificuldade), checar_diagonal(matrizoculta, dificuldade), dificuldade)
            rodada = 1 # Muda a rodada para que o jogador2 jogue na próxima.
        else: # Alternancia de rodada, quando a rodada é 1 o jogador2 ganha os pontos caso complete uma linha/coluna/diagonal
            jogador2 += somar_pontos(checar_linha(matrizoculta, dificuldade), checar_coluna(matrizoculta, dificuldade), checar_diagonal(matrizoculta, dificuldade), dificuldade)
            rodada = 0 # Muda a rodada para que o jogador1 jogue na próxima.
        print(f"A pontuação do jogador 1 é de {jogador1} pontos")
        divisores()
        print(f"A pontuação do jogador 2 é de {jogador2} pontos")
        divisores()
        fim_jogo = definir_vencedor(matrizoculta, jogador1, jogador2, dificuldade) # Recebe da função o vencedor.
        if fim_jogo is not False: # Caso há um vencedor, fim_jogo vai ser diferente de Falso e vai entrar em outra condição.
            if fim_jogo == "jogador 1" or fim_jogo == "jogador 2": # Aqui decide o vencedor de acordo com o retorno da função.
                print(f"O vencedor do jogo foi o {fim_jogo}.")
            else: # Caso há empate, (sim, é possível.)
                print("O jogo deu empate.")
            loop = False

matrizjogo, matrizoculta, dificuldade = escolha_dificuldade() # Aqui as principais váriaveis são definidas para o início do jogo.
main() # Aqui o programa principal é chamado.
