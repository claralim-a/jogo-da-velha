import random
from old.functions import printMatrix, JogarNovamente

# Pontuacao inicial
global pontuacao_jogador, pontuacao_computador
pontuacao_jogador = 0
pontuacao_computador = 0
     
# =============================================
def ComputerAlgorithm(jogador, computador):
    
    # 1. Para ganhar =====================================================
    # Se o computador tiver dois valores em uma linha
    for i in range(3):
        qtd_computador = matriz[i].count(computador) # Conta 'O' em cada linha
        qtd_disp = matriz[i].count('-') # Conta espaços vazios
        
        if qtd_computador == 2 and qtd_disp == 1: # Se há O O e um espaço disponível, joga neste espaço
            valor_disp_linha = [v for v in valores_disponiveis if v[0] == i and matriz[v[0]][v[1]] == '-']
            # print('valor_disp_linha[0]')
            return valor_disp_linha[0]
    
    # Se o computador tiver dois valores em uma coluna
    for j in range(3):
        coluna = [linha[j] for linha in matriz]
        qtd_computador = coluna.count(computador) # Conta O na coluna
        qtd_disp = coluna.count('-') # Conta espaços vazios
        # print(f'COLUNA {j} - qtd_computador: {qtd_computador}, qtd_disp: {qtd_disp}')     
        if qtd_computador == 2 and qtd_disp == 1:
            valor_disp_col = [v for v in valores_disponiveis if v[1] == j and matriz[v[0]][v[1]] == '-']
            if valor_disp_col:
                # print('valor_disp_col[0]')
                return valor_disp_col[0]
                

    # Se o computador tiver dois valores na diagonal
    # Principal
    diag_princ_list = [matriz[0][0], matriz[1][1], matriz[2][2]]
    qtd_computador_diag_princ = diag_princ_list.count(computador)
    qtd_disp_diag_princ = diag_princ_list.count('-')

    if qtd_computador_diag_princ == 2 and qtd_disp_diag_princ == 1:
        for k in range(3):
            if matriz[k][k] == '-':
                # print('(k,k)')
                return (k,k)

    # Secundária
    diag_sec_list = [matriz[0][2], matriz[1][1], matriz[2][0]]
    qtd_computador_diag_sec = diag_sec_list.count(computador)
    qtd_disp_diag_sec = diag_sec_list.count('-')
    if qtd_computador_diag_sec == 2 and qtd_disp_diag_sec == 1:
        for k in range(3):
                    if matriz[k][2 - k] == '-':
                        # print('(k, 2-k)')
                        return (k, 2 - k)


    # 2. Para evitar perda =====================================================
    # Se o usuario tiver dois valores em uma linha
    for i in range(3):
        qtd_jogador = matriz[i].count(jogador)
        qtd_disp = matriz[i].count('-')
        if qtd_jogador == 2 and qtd_disp == 1:
            valor_disp_linha = [v for v in valores_disponiveis if v[0] == i and matriz[v[0]][v[1]] == '-']
            # print('valor_disp_linha[0] computador')
            return valor_disp_linha[0]
    
    # Se o usuario tiver dois valores em uma coluna
    for j in range(3):
        coluna = [linha[j] for linha in matriz]
        qtd_jogador = coluna.count(jogador)
        qtd_disp = coluna.count('-')
        # print(f'COLUNA {j} - qtd_jogador: {qtd_jogador}, qtd_disp: {qtd_disp}')   

        if qtd_jogador == 2 and qtd_disp == 1:
            valor_disp_col = [v for v in valores_disponiveis if v[1] == j and matriz[v[0]][v[1]] == '-']
            # print('valor_disp_col[0] computador')
            return valor_disp_col[0]

    # Se o usuario tiver dois valores na diagonal
    # Principal
    diag_princ_list = [matriz[0][0], matriz[1][1], matriz[2][2]]
    qtd_jogador_diag_princ = diag_princ_list.count(jogador)
    qtd_disp_diag_princ = diag_princ_list.count('-')
    if qtd_jogador_diag_princ == 2 and qtd_disp_diag_princ == 1:
        for k in range(3):
            if matriz[k][k] == '-':
                # print('(k,k) computador')
                return (k,k)
    
    # Secundária
    diag_sec_list = [matriz[0][2], matriz[1][1], matriz[2][0]]
    qtd_jogador_diag_sec = diag_sec_list.count(jogador)
    qtd_disp_diag_sec = diag_sec_list.count('-')
    if qtd_jogador_diag_sec == 2 and qtd_disp_diag_sec == 1:
        for k in range(3):
                    if matriz[k][2 - k] == '-':
                        # print('(k, 2-k) computador')
                        return (k, 2 - k)
    
    # 3. Primeira jogada
    cantos = [(0,0),(0,2), (2,0), (2,2)]
    cantos_disponiveis = [v for v in cantos if v in valores_disponiveis]
    if cantos_disponiveis:
        # print('random.choice(cantos_disponiveis)')
        return random.choice(cantos_disponiveis)
    elif valores_disponiveis:
        # print('random.choice(valores_disponiveis)')
        return random.choice(valores_disponiveis)
    
# Matriz
matriz = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
valores_disponiveis = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

# Status
status = True

again = 1
print('\n=================================')
print('Seja bem vindo ao Jogo da Velha!')
print('=================================\n')

# Definir qual simbolo
jogador = input('Você deseja ser X ou O? (X/O)')
# Opção inválida, Default 'X
if jogador not in ['X', 'O', 'x', 'o']:
    print('\nOpção inválida. Você será o X e o computador será o O.')
    jogador = 'X'
    computador = 'O'
else:
    if jogador == 'X' or jogador == 'x':
        jogador = jogador.upper()
        computador = 'O'
    else:
        jogador = jogador.upper()
        computador = 'X'


# Definir o nivel de dificuldade
dificuldade = int(input('Selecione o nível de dificuldade: 1 - Fácil | 2 - Médio | 3 - Difícil'))
if dificuldade == 1:
    fator_aleatoriedade = 0.20
elif dificuldade == 2:
    fator_aleatoriedade = 0.15
elif dificuldade == 3:
    fator_aleatoriedade = 0.005
else:
    print('Opção inválida. Você jogará à dificuldade fácil.')
    fator_aleatoriedade = 0.5




printMatrix(matriz)


# print('\nTabuleiro:\n')
# for linha in matriz:
#         print(" ".join(f"{x:3}" for x in linha))

# Roda o loop ================================================================
while again == 1:

    # Jogada usuário
    linha_jogada = int(input('\nDigite qual linha vc quer jogar (0-2)'))
    coluna_jogada = int(input('Digite qual coluna vc quer jogar (0-2)'))
    jogada_usuario = (linha_jogada, coluna_jogada)

    if jogada_usuario in valores_disponiveis:
        matriz[linha_jogada][coluna_jogada] = jogador
        print('\nSua jogada:\n')
        printMatrix(matriz)

        valores_disponiveis.remove(jogada_usuario)
    else: 
        print('Essa jogada não pode ser feita. Tente novamente')
        linha_jogada = int(input('\nDigite qual linha vc quer jogar (0-2)'))
        coluna_jogada = int(input('Digite qual coluna vc quer jogar (0-2)'))
        jogada_usuario = (linha_jogada, coluna_jogada)
        if jogada_usuario in valores_disponiveis:
            matriz[linha_jogada][coluna_jogada] = jogador
            print('\nSua jogada:\n')
            printMatrix(matriz)

            valores_disponiveis.remove(jogada_usuario)
        else:
            print('Essa jogada não pode ser feita. Saindo do jogo.')
            break
    
    # Jogada computador
    if random.random() <= fator_aleatoriedade: # Gera um número entre 0 e 1
        jogada_computador = random.choice(valores_disponiveis)
    else:
        jogada_computador = ComputerAlgorithm(jogador, computador)

    if valores_disponiveis:
        matriz[jogada_computador[0]][jogada_computador[1]] = computador
        valores_disponiveis.remove(jogada_computador)
        print('\nJogada do computador:\n')
    
        printMatrix(matriz)
    

    # Usuário vence ======================================================================
    # Linhas
    for i in range(3):
        if (matriz[i][0] == jogador and matriz[i][1] == jogador and matriz[i][2] == jogador):
            print('\nVocê venceu!')
            pontuacao_jogador += 1
            # Printa a pontuação
            print('\nPontuação:')
            print(f'- Você: {pontuacao_jogador}')
            print(f'- Computador: {pontuacao_computador}')

            jogar_novamente = input('Deseja jogar novamente? (s/n)')
            if jogar_novamente == 's':
                matriz, valores_disponiveis = JogarNovamente()
                continue
            elif jogar_novamente == 'n':
                again = 0
                break       

    # Colunas
    for j in range(3):
        if matriz[0][j] == jogador and matriz[1][j] == jogador and matriz[2][j] == jogador:
            print('\nVocê venceu!')
            pontuacao_jogador += 1
            # Printa a pontuação
            print('\nPontuação:')
            print(f'- Você: {pontuacao_jogador}')
            print(f'- Computador: {pontuacao_computador}')
            # valores_disponiveis = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

            jogar_novamente = input('Deseja jogar novamente? (s/n)')
            if jogar_novamente == 's':
                matriz, valores_disponiveis = JogarNovamente()
                continue
            elif jogar_novamente == 'n':
                again = 0
                break   

    # Diagonais
    if (matriz[0][0] == jogador and matriz[1][1] == jogador and matriz[2][2] == jogador) or (matriz[0][2] == jogador and matriz[1][1] == jogador and matriz[2][0] == jogador):
        print('\nVocê venceu!')
        pontuacao_jogador += 1
        # Printa a pontuação
        print('\nPontuação:')
        print(f'- Você: {pontuacao_jogador}')
        print(f'- Computador: {pontuacao_computador}')
        # valores_disponiveis = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

        jogar_novamente = input('Deseja jogar novamente? (s/n)')
        if jogar_novamente == 's':
            matriz, valores_disponiveis = JogarNovamente()
            continue
        elif jogar_novamente == 'n':
            again = 0
            break   

    # Computador vence ======================================================================
    # Linhas
    for i in range(3):
        if matriz[i][0] == computador and matriz[i][1] == computador and matriz[i][2] == computador:
            print('\nVocê perdeu!')
            # valores_disponiveis = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
            pontuacao_computador += 1

            # Printa a pontuação
            print('\nPontuação:')
            print(f'- Você: {pontuacao_jogador}')
            print(f'- Computador: {pontuacao_computador}')

            jogar_novamente = input('Deseja jogar novamente? (s/n)')
            if jogar_novamente == 's':
                matriz, valores_disponiveis = JogarNovamente()
                continue
            elif jogar_novamente == 'n':
                again = 0
                break   

    # Colunas
    for j in range(3):
        if matriz[0][j] == computador and matriz[1][j] == computador and matriz[2][j] == computador:
            print('\nVocê perdeu!')
            pontuacao_computador += 1

            # Printa a pontuação
            print('\nPontuação:')
            print(f'- Você: {pontuacao_jogador}')
            print(f'- Computador: {pontuacao_computador}')

            jogar_novamente = input('Deseja jogar novamente? (s/n)')
            if jogar_novamente == 's':
                matriz, valores_disponiveis = JogarNovamente()
                continue
            elif jogar_novamente == 'n':
                again = 0
                break   

    # Diagonais
    if (matriz[0][0] == computador and matriz[1][1] == computador and matriz[2][2] == computador) or (matriz[0][2] == computador and matriz[1][1] == computador and matriz[2][0] == computador):
        print('\nVocê perdeu!')
        pontuacao_computador += 1
        # Printa a pontuação
        print('\nPontuação:')
        print(f'- Você: {pontuacao_jogador}')
        print(f'- Computador: {pontuacao_computador}')
        # valores_disponiveis = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

        jogar_novamente = input('Deseja jogar novamente? (s/n)')
        if jogar_novamente == 's':
            matriz, valores_disponiveis = JogarNovamente()
            continue
        elif jogar_novamente == 'n':
            again = 0
            break   

    # Empate ===================================================================================
    if not valores_disponiveis:
        print('\nEmpate!')
        # Printa a pontuação
        print('\nPontuação:')
        print(f'- Você: {pontuacao_jogador}')
        print(f'- Computador: {pontuacao_computador}')

        jogar_novamente = input('Deseja jogar novamente? (s/n)')
        if jogar_novamente == 's':
            matriz, valores_disponiveis = JogarNovamente()
            continue
        elif jogar_novamente == 'n':
            again = 0
            break   