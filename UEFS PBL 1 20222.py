#Autor: Diogo dos Santos de Jesus
#Componente Curricular: Algoritmos I
#Concluído em: 24/09/2022
#Declaro que este código foi elaborado por mim de forma individual e não contém
#nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
#código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

menu_loop = True # Váriavel usada para fazer o loop do menu.
area_total = 0 # Váriavel usada para armazenar a área total reflorestada da região Nordeste.
area_comparacao = 0 # Váriavel utilizada para comparar à área digitada pelo usuário.
area_adicionada = 0 # Variável utilizada para verificar se uma área foi adicionada.
arvores_comparacao_maior = arvores_comparacao_menor = 0 # Váriaveis usadas para armazenar o valor da maior e menor área de arvores e usar como comparação caso necessite de uma troca.
estado_comparacao_maior = estado_comparacao_menor = 0 # Váriaveis usadas para armazenar o valor da maior e menor área de estados e usar como comparação caso necessite de uma troca.
estados = {"Alagoas": 0, "Bahia": 0, "Ceara": 0, "Maranhao": 0, "Paraiba": 0, # Dicionário utilizado para guardar os valores das áreas dos estados.
"Pernambuco": 0, "Piaui": 0, "Rio Grande do Norte": 0, "Sergipe": 0}

qtd_area_por_estado = {"Alagoas": 0, "Bahia": 0, # Dicionário utilizado para guardar a quantidades de áreas que cada estado tem.
"Ceara": 0, "Maranhao": 0, "Paraiba": 0,
"Pernambuco": 0, "Piaui": 0, "Rio Grande do Norte": 0, "Sergipe": 0}

estados_nome = ["Alagoas", "Bahia", "Ceara", "Maranhao", "Paraiba", # Lista utilizada para guardar os nomes de estado, para facilitar em comparações ou prints.
"Pernambuco", "Piaui", "Rio Grande do Norte", "Sergipe"]

arvores = {"Cajueiro": 0, "Mangueira": 0, "Dende": 0, "Coqueiro": 0, "Bambu gigante": 0, "Ipe": 0} # Dicionário utilizado para guardar as áreas da árvore

qtd_arvores = {"Cajueiro": 0, "Mangueira": 0, "Dende": 0, "Coqueiro": 0, "Bambu gigante": 0, "Ipe": 0} # Dicionário utilizado para guardar a quantidades de vezes que um tipo de árvore foi utilizada.

arvores_nome = ["Cajueiro", "Mangueira", "Dende", "Coqueiro", "Bambu gigante", "Ipe"] # Lista utilizada para guardar os nomes dos tipos de árvore, para facilitar comparação e prints.

maior_area_reflorestada = {"Código de área": 0,
"Estado": 0,"Cidade": 0, "Área": 0, "Tipo de árvore": 0} # Dicionário utilizado para guardar as informações da maior área reflorestada.

codigos_areas = [] # Lista utilizada para guardar os codigos de área.

while menu_loop is True: # Um loop que vai rodar até o usuário decidir terminar.
    nao_reflorestados = False # Váriavel utilizada para verificar.
    aux_contagem_estado = 1 # Auxiliar utilizada para ordenar os estados por número nos prints.
    aux_contagem_arvore = 1 # Auxiliar utilizada para ordenar os tipos de árvore por número nos prints.
    aux_area = True # Váriavel usada em um loop como condicional.
    codigo_checar = 1 # Váriavel usada em um loop como condicional.
    print("="*65) # Esse print foi utilizado diversas vezes no programa com o objetivo de deixar uma interface mais bonita e organizada.
    print(f'{"Sistema de Gerenciamento de Reflorestamento":^65}')
    print("="*65)
    print("1) Adicionar uma área.")
    print("2) Mostrar relatório.")
    print("0) Sair do programa.")
    opcao = input("Escolha uma opção(0-2): ") # Váriavel utilizada para que o usuário consiga navegar no menu ou encerrar o programa.
    print("="*65)
    if opcao == "1": # Primeira opção do menu, onde o usuário consegue adicionar uma área.
        codigo_area = input("Escolha um código para área: ") # Pede ao usuário um código para a área.
        while codigo_checar == 1: # Loop que vai repetir até que o usuário coloque um código de área que não tenha sido colocado antes.
            if codigo_area not in codigos_areas: # Checa se o código inserido pelo usuário já está na lista, se não estiver, o codigo é adicionado a lista de codigos_areas e o loop é encerrado.
                codigos_areas.append(codigo_area) # Adiciona o código inserido pelo usuário na lista que posteriormente será usada para checar.
                codigo_checar = 0 # Encerra o loop.
            else: # Caso o usuário tenha inserido um codigo de área já existente ná lista de codigos_areas será mostrar uma mensagem mostrando que o código já foi inserido e pedirá outro código, isso irá se repetir até que o usuário digite um código que não esteja na lista.
                print("Esse código de área já existe.")
                codigo_area = input("Escolha um código para área: ")
        print("="*65)
        for nome_estado in estados: # Loop for utilizado para iterar sobre os nomes das chaves do dicionário estado e printar eles enumerados um embaixo do outro.
            print(f"{aux_contagem_estado}) {nome_estado}") # Print para mostrar o estado com seu respectivo numero.
            aux_contagem_estado += 1 # Auxiliar irá enumerar os estados, logo, ela é somada a cada vez que o loop for roda.
        estado = input("Estado onde a área está localizada(1-9): ") # Essa váriavel armazena a estado digitada de onde a área está localizada, aqui o usuário escolhe uma das opções de estado(1-9) mostrada pelo print.
        print("="*65)
        while not estado.isnumeric() or int(estado) > 9 or int(estado) < 1: # Faz uma verificação que observa se o input do "estado" colocado pelo usuário está respeitando as regras, de ser um número maior que zero e menor que dez.
            print("Opção inválida.")
            estado = input("Digite uma opção válida: ")
            print("="*65)
        estado = int(estado)
        cidade = input("Sigla da cidade de onde a área está localizada: ") # Essa váriavel armazena a sigla da cidade digitada de onde a área está localizada.
        print("="*65)
        while aux_area is True: # enquanto um valor inválido ser colocado nesse input, haverá uma repetição até que o usuário coloque um correto
            try:
                base, altura = map(eval, input("Dimensões da área(base e altura): ").split())
                print("="*65)
                while not isinstance(base, (float, int)) or not isinstance(altura, (float, int)) or float(base) <= 0 or float(altura) <= 0: #Checa se é float ou int
                    print("Base e altura inválidos.")
                    base, altura = map(eval, input("Digite novamente as dimensões: ").split())
                    print("="*65)
                if isinstance(base, (float, int)) and isinstance(altura, (float, int)): #Checa se é float ou int
                    aux_area = False
            except (ValueError, SyntaxError, NameError): #Caso o usuario digite uma string o except vai mostrar essas mensagens
                print("Base e altura inválidos.")
                print("="*65)
        area_input = float(base) * float(altura) # Aqui há o cálculo da área.
        area_total += area_input # Soma-se a area digitada pelo usuário nessa váriavel
        for nome_arvore in arvores: # Mostra os tipos de arvores
            print(f"{aux_contagem_arvore}) {nome_arvore}")
            aux_contagem_arvore += 1
        tipo_arvore = input("Tipo de árvore usado para o reflorestamento(1-6): ") # pede o tipo de arvore
        print("="*65)
        while not tipo_arvore.isnumeric() or int(tipo_arvore) > 6 or int(tipo_arvore) < 1: # Checa se uma opção válida foi digitada.
            print("Opção inválida.")
            tipo_arvore = input("Digite uma opção válida: ")
            print("="*65)
        tipo_arvore = int(tipo_arvore) # Transforma a str do tipo de arvore em um inteiro.
        print(f'{"Área":>20} {codigo_area} {"foi adicionada com sucesso."}')
        area_adicionada += 1 # Soma-se um nessa váriavel para que seja possível mostrar o relatório.
        if area_input > area_comparacao: # Se as dimensoes da area digitada pelo usuário ser maior que a da comparação, as informações da área serão armazenadas nesse dicionário.
            maior_area_reflorestada = {
            "Código de área": codigo_area,
            "Estado": estados_nome[estado-1],
            "Cidade": cidade,
            "Área": f"{area_input} km²",
            "Tipo de árvore": arvores_nome[tipo_arvore-1]
            }
            area_comparacao = area_input
        for estados_nome_itens in estados_nome: # Como foi utilizado números para que o usuário selecione o estado e as árvores, foi criada uma lista com os mesmos nomes do dicionário.
            if estados_nome.index(estados_nome_itens) == estado-1: # O que acontece aqui é que se o numero do estado digitado pelo usuário for igual ao index da lista, será adicionado na respectiva chave.
                estados[estados_nome_itens] += area_input
                qtd_area_por_estado[estados_nome_itens] += 1
        for arvores_itens in arvores:
            if arvores_nome.index(arvores_itens) == tipo_arvore-1: # O que acontece aqui é que se o numero do tipo de árvore digitado pelo usuário for igual ao index da lista, será adicionado na respectiva chave.
                arvores[arvores_itens] += area_input
                qtd_arvores[arvores_itens] += 1
        for contador_arvore in qtd_arvores:
            if qtd_arvores[contador_arvore] > arvores_comparacao_maior: # Aqui ocorre as comparações para descobrir qual árvore foi a mais utilizada.
                arvores_comparacao_maior = qtd_arvores[contador_arvore]
                arvores_comparacao_menor = qtd_arvores[contador_arvore]
                maior_arvore = contador_arvore
                if area_adicionada == 1: # Para que haja uma comparação, o menor valor na primeira rodagem do programa será o maior também.
                    menor_arvore = maior_arvore
        for contador_arvore in qtd_arvores:
            if qtd_arvores[contador_arvore] < arvores_comparacao_menor and qtd_arvores[contador_arvore] > 0: # Utilizado para descobrir a quantidade de arvore menos utilizada. (ignorando as arvores que ainda não foram utilizadas.)
                arvores_comparacao_menor = qtd_arvores[contador_arvore]
                menor_arvore = contador_arvore
        for estados_itensc in estados:
            if estados[estados_itensc] >= estado_comparacao_maior: # Aqui ocorre as comparações para descobrir qual árvore foi a mais utilizada.
                estado_comparacao_maior = estados[estados_itensc]
                estado_comparacao_menor = estados[estados_itensc]
                maior_estado = estados_itensc
                if area_adicionada == 1: # Para que haja uma comparação, o menor valor na primeira rodagem do programa será o maior também.
                    menor_estado = estados_itensc
        for estados_itensc in estados:
            if estados[estados_itensc] < estado_comparacao_menor and estados[estados_itensc] > 0: # Utilizado para descobrir o estado menos reflorestado. (ignorando os estados que ainda não foram reflorestados.)
                estado_comparacao_menor = estados[estados_itensc]
                menor_estado = estados_itensc
    elif opcao == "2": # Será mostrado o relatório.
        if area_adicionada > 0: # Caso seja adicionada uma área, o relatório será mostrado normalmente.
            print(f'{"Área total reflorestada por estado":^65}')
            print("="*65)
            for estados_chaves in estados: # Aqui a chave itera sobre os estados e mostra-os com seu respectivo valor de área.
                print(f"{estados_chaves}: {estados[estados_chaves]:.2f} km²")
            print("="*65)
            print(f'{"Área total reflorestada na Região Nordeste:":>50} {area_total:.0f} km²')
            print("="*65)
            print(f'{"Área total reflorestada por cada tipo de árvore":^65}')
            print("="*65)
            for arvores_chave in arvores: # Aqui a chave itera sobre os arvores e mostra-os com seu respectivo valor de área.
                print(f"{arvores_chave}: {arvores[arvores_chave]:.2f} km²")
            print("="*65)
            print(f'{"Tipo de árvore mais utilizado: " + maior_arvore:^65}')
            print("="*65)
            print(f'{"Tipo de árvore menos utilizado: " + menor_arvore:^65}')
            print("="*65)
            print(f'{"Informações da maior área reflorestada":^65}')
            print("="*65)
            for maior_area_chaves in maior_area_reflorestada: # Aqui a chave itera sobre o dicionário da maior área reflorestado, e mostra-os.
                print(f"{maior_area_chaves}: {maior_area_reflorestada[maior_area_chaves]}")
            print("="*65)
            print(f'{"Quantidade de áreas por estado":^65}')
            print("="*65)
            for qtd_area_chaves in qtd_area_por_estado: # Aqui a chave itera sobre o dicionário de quantidade de área por estado, e mostra a quantidade de vezes que foram utilizados.
                print(f"{qtd_area_chaves}: {qtd_area_por_estado[qtd_area_chaves]}")
            print("="*65)
            print(f"{'Estado menos reflorestado: '+ menor_estado:^65}")
            print("="*65)
            print(f"{'Estados que ainda não foram reflorestados':^65}")
            print("="*65)
            for naoreflo_chaves in estados: # Aqui vai rodar no dicionário estado e vai printar somente se for igual a zero.
                if estados[naoreflo_chaves] == 0:
                    print(naoreflo_chaves)
                    nao_reflorestados = True # Variável que checa se há estados não reflorestados.
            if nao_reflorestados is False: # Caso não haja estados que ainda não foram refloresetados, será mostrada a mensagem abaixo.
                print("Todos os estados foram reflorestados.")
        else: # Caso o usuário tente rodar sem ter adicionada uma area
            print(f'{"Nenhuma área foi adicionada ainda!":^65}')
    elif opcao == "0": # Se o usuário digitar zero a váriavel do menu_loop sera mudada para falsa e ira cair.
        menu_loop = False
    