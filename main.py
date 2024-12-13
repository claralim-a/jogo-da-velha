# cd C:\Users\User\OneDrive\Documentos\Pessoal\DataScience\AsimovAcademy\PythonStarter\JogoDaVelha
# py main.py

import random

# Classe JogoDaVelha
class JogoDaVelha:
    '''

    A classe JogoDaVelha comporta os componentes do jogo:
    - __init__;
    - exibir_tabuleiro;
    - determinar_aleatoriedade;
    - resetar_jogo;
    - verificar_vencedor;
    - verificar_empate;
    - atualizar_pontuacao;
    - exibir_pontuacao.

    '''

    def __init__(self, fator_aleatoriedade=0.2):
        self.tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.jogadas_disponiveis = [(i, j) for i in range(3) for j in range(3)]
        self.fator_aleatoriedade = fator_aleatoriedade      
        self.pontos_jogador = 0
        self.pontos_computador = 0

    def exibir_tabuleiro(self):
        print("   0   1   2")
        for i, linha in enumerate(self.tabuleiro):
            print(f"{i}  {' | '.join(linha)}")
            if i < 2:
                print("  ---+---+---")

    def determinar_aleatoriedade(self):
        dificuldade = input('Selecione o nível de dificuldade: 1 - Fácil | 2 - Médio | 3 - Difícil')
        
        while dificuldade not in ['1','2','3']:
            print('Escolha inválida. Tente novamente.')
            dificuldade = input('Selecione o nível de dificuldade: 1 - Fácil | 2 - Médio | 3 - Difícil')
        self.dificuldade = dificuldade

        if dificuldade == '1':
            return 0.2
        elif dificuldade == '2':
            return 0.1
        elif dificuldade == '3':
            return 0
        
    def resetar_jogo(self):
        self.tabuleiro = [[" ", " ", " "] for _ in range(3)]
        self.jogadas_disponiveis = [(i, j) for i in range(3) for j in range(3)]

    def verificar_vencedor(self, simbolo):
        # Verifica linhas, colunas e diagonais
        for i in range(3):
            if all(self.tabuleiro[i][j] == simbolo for j in range(3)):  # Linha
                return True
            if all(self.tabuleiro[j][i] == simbolo for j in range(3)):  # Coluna
                return True
        if all(self.tabuleiro[i][i] == simbolo for i in range(3)):  # Diagonal principal
            return True
        if all(self.tabuleiro[i][2 - i] == simbolo for i in range(3)):  # Diagonal secundária
            return True
        return False

    def verificar_empate(self):
        return not self.jogadas_disponiveis

    def atualizar_pontuacao(self, vencedor):
        if vencedor == "jogador":
            self.pontos_jogador += 1
        elif vencedor == "computador":
            self.pontos_computador += 1

    def exibir_pontuacao(self):
        print("\nPontuação:")
        print(f"Jogador: {self.pontos_jogador}")
        print(f"Computador: {self.pontos_computador}")


# Classe do jogador
class Usuario:
    '''
    
    A classe Usuario comporta os componentes do Usuario:
    
    - __init__;
    - escolher_simbolo;
    - realizar_jogada.

    '''
    def __init__(self):
        self.simbolo = ""

    def escolher_simbolo(self):
        simbolo = input("Você deseja ser X ou O? ").upper()
        while simbolo not in ["X", "O"]:
            print("Escolha inválida. Tente novamente.")
            simbolo = input("Você deseja ser X ou O? ").upper()
        self.simbolo = simbolo
        return self.simbolo

    def realizar_jogada(self, jogadas_disponiveis):
        while True:
            try:
                linha = int(input("Digite a linha (0-2): "))
                coluna = int(input("Digite a coluna (0-2): "))
                if (linha, coluna) in jogadas_disponiveis:
                    return linha, coluna
                else:
                    print("Jogada inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite números entre 0 e 2.")


class Computador:
    '''
    
    A classe Computador comporta os componentes do Computador:

    - __init__;
    - realizar_jogada;
    
    '''
    def __init__(self, simbolo, jogo):
        self.simbolo = simbolo
        self.jogo = jogo  # Referência à instância de JogoDaVelha

    def realizar_jogada(self, jogadas_disponiveis, fator_aleatoriedade, tabuleiro, simbolo_oponente):
        # Joga aleatoriamente se dentro do fator de aleatoriedade
        if random.random() <= fator_aleatoriedade:
            return random.choice(jogadas_disponiveis)

        # Tenta encontrar uma jogada vencedora
        for jogada in jogadas_disponiveis:
            linha, coluna = jogada
            tabuleiro[linha][coluna] = self.simbolo  # Simula a jogada do computador
            if self.jogo.verificar_vencedor(self.simbolo):  # Verifica vitória
                tabuleiro[linha][coluna] = " "  # Desfaz a simulação
                return jogada
            tabuleiro[linha][coluna] = " "  # Desfaz a simulação

        # Tenta bloquear o jogador
        for jogada in jogadas_disponiveis:
            linha, coluna = jogada
            tabuleiro[linha][coluna] = simbolo_oponente  # Simula a jogada do oponente
            if self.jogo.verificar_vencedor(simbolo_oponente):  # Verifica se jogador pode vencer
                tabuleiro[linha][coluna] = " "  # Desfaz a simulação
                return jogada
            tabuleiro[linha][coluna] = " "  # Desfaz a simulação

        # Caso nenhuma jogada de vitória ou impedir derrota seja encontrada, joga na diagonal ou meio
        diagonais = [(0,0), (0,2), (1,1), (2,0), (2,2)]
        jogadas_diagonal_disponiveis = [jogada for jogada in jogadas_disponiveis if jogada in diagonais]

        if jogadas_diagonal_disponiveis:
            return random.choice(jogadas_diagonal_disponiveis)
        
        # Caso nenhuma jogada estratégica seja encontrada, escolhe aleatoriamente
        return random.choice(jogadas_disponiveis)


# Função principal
def main():
    jogo = JogoDaVelha()
    jogador = Usuario()
    jogador_simbolo = jogador.escolher_simbolo()
    computador = Computador("O" if jogador_simbolo == "X" else "X", jogo)  # Passa a instância
    fator_aleatoriedade = jogo.determinar_aleatoriedade()
    jogo.fator_aleatoriedade = fator_aleatoriedade
    print(f"Fator de aleatoriedade configurado: {fator_aleatoriedade}")

    while True:
        jogo.resetar_jogo()
        print("\nNovo Jogo!")
        jogo.exibir_tabuleiro()

        while True:
            # Jogada do jogador
            print("\nSua vez:")
            linha, coluna = jogador.realizar_jogada(jogo.jogadas_disponiveis)
            jogo.tabuleiro[linha][coluna] = jogador.simbolo
            jogo.jogadas_disponiveis.remove((linha, coluna))
            jogo.exibir_tabuleiro()

            if jogo.verificar_vencedor(jogador.simbolo):
                print("\nParabéns, você venceu!")
                jogo.atualizar_pontuacao("jogador")
                break
            if jogo.verificar_empate():
                print("\nEmpate!")
                break

            # Jogada do computador
            print("\nVez do computador:")
            linha, coluna = computador.realizar_jogada(
                jogo.jogadas_disponiveis,
                jogo.fator_aleatoriedade,
                jogo.tabuleiro,
                jogador.simbolo,
            )
            jogo.tabuleiro[linha][coluna] = computador.simbolo
            jogo.jogadas_disponiveis.remove((linha, coluna))
            jogo.exibir_tabuleiro()

            if jogo.verificar_vencedor(computador.simbolo):
                print("\nVocê perdeu!")
                jogo.atualizar_pontuacao("computador")
                break
            if jogo.verificar_empate():
                print("\nEmpate!")
                break

        jogo.exibir_pontuacao()
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        while jogar_novamente not in ["s", "n"]:
            print("Escolha inválida. Tente novamente.")
            jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()

        if jogar_novamente == "n":
            print("Obrigado por jogar!")
            break

if __name__ == "__main__":
    main()
