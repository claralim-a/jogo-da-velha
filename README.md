# Jogo da Velha - Documentação

Este repositório contém um código Python para jogar o **Jogo da Velha** contra o computador. O jogo oferece diferentes níveis de dificuldade, variando a aleatoriedade das jogadas do computador. O jogador pode escolher seu símbolo (X ou O), e o computador tenta jogar de forma estratégica.

## Objetivo

Desenvolvi este projeto para aprimorar as minhas habilidades em lógica de programação, python e programação orientada a objetos. Foi um projeto divertido de executar!

## Estrutura do Código

### Classes

#### 1. **Classe `JogoDaVelha`**

Responsável pela lógica do jogo e controle do tabuleiro. Contém as funções principais para inicializar o jogo, exibir o tabuleiro, verificar vitórias e empates, além de manter a pontuação.

**Métodos:**
- `__init__(self, fator_aleatoriedade=0.2)`: Inicializa o tabuleiro, o fator de aleatoriedade e as pontuações.
- `exibir_tabuleiro(self)`: Exibe o tabuleiro no terminal.
- `determinar_aleatoriedade(self)`: Define o nível de dificuldade do jogo e retorna o fator de aleatoriedade (probabilidade de jogadas aleatórias do computador).
- `resetar_jogo(self)`: Reseta o tabuleiro e as jogadas disponíveis.
- `verificar_vencedor(self, simbolo)`: Verifica se um jogador venceu o jogo (linhas, colunas ou diagonais).
- `verificar_empate(self)`: Verifica se o jogo terminou em empate (sem jogadas disponíveis).
- `atualizar_pontuacao(self, vencedor)`: Atualiza a pontuação do jogador ou computador.
- `exibir_pontuacao(self)`: Exibe a pontuação atual de jogador e computador.

#### 2. **Classe `Usuario`**

Representa o jogador humano. Permite que ele escolha seu símbolo e faça jogadas.

**Métodos:**
- `__init__(self)`: Inicializa o símbolo do jogador.
- `escolher_simbolo(self)`: Solicita ao jogador escolher entre 'X' ou 'O'.
- `realizar_jogada(self, jogadas_disponiveis)`: Solicita ao jogador escolher uma posição no tabuleiro para sua jogada.

#### 3. **Classe `Computador`**

Representa a inteligência artificial do computador. A IA faz suas jogadas com base em aleatoriedade e estratégia para vencer ou bloquear o jogador.

**Métodos:**
- `__init__(self, simbolo, jogo)`: Inicializa o símbolo do computador e a referência ao objeto de jogo.
- `realizar_jogada(self, jogadas_disponiveis, fator_aleatoriedade, tabuleiro, simbolo_oponente)`: Faz a jogada do computador, considerando o fator de aleatoriedade e tentando bloquear ou vencer o jogador.

### Função Principal

A função `main()` coordena o jogo, alternando turnos entre o jogador e o computador. Ela inicializa as instâncias de `JogoDaVelha`, `Usuario` e `Computador`, além de gerenciar o fluxo do jogo (reseta o jogo, exibe o tabuleiro, e verifica condições de vitória ou empate).

**Fluxo:**
1. O jogador escolhe seu símbolo.
2. O computador escolhe seu símbolo e o nível de dificuldade é determinado.
3. O jogo começa e as jogadas alternam entre o jogador e o computador até que haja um vencedor ou empate.
4. A pontuação é atualizada e o jogador é questionado se deseja jogar novamente.

### Execução

Para rodar o jogo, execute o seguinte comando no terminal:

```bash
py main.py
