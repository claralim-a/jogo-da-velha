# Redefine as variáveis para jogar de novo
def JogarNovamente():
    matriz = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    valores_disponiveis = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    
    return matriz, valores_disponiveis

# Printa o tabulero com os indices das linhas e colunas
def printMatrix(matriz):
    # Índice da coluna
    print("    ", end="")  # Espaço inicial para alinhar com os índices das linhas
    for col in range(len(matriz[0])):
        print(f" {col} ", end="")
    print("\n")  # Pular uma linha após os índices das colunas

    # Imprimir a matriz com os índices das linhas e espaçamento ajustado
    for i, row in enumerate(matriz):
        print(f"{i}   ", end="")  # Índice da linha com mais espaço
        for element in row:
            print(f" {element} ", end="")
        print()