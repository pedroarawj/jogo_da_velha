from random import randint
from jogador import Jogador
from tabuleiro import Tabuleiro
import copy

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def R1(self, oponente):
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    self.matriz[l][c] = self.tipo
                    if self.tabuleiro.tem_campeao() == self.tipo:
                        self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                        return (l, c)
                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO

                    self.matriz[l][c] = oponente
                    if self.tabuleiro.tem_campeao() == oponente:
                        self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                        return (l, c)
                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO


    def R2(self):
        #R2
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    simulacao = copy.deepcopy(self.matriz)
                    simulacao[l][c] = self.tipo
                    passos_vitoria = 0
                    for i in range(3):
                        # Linha
                        if simulacao[i].count(self.tipo) == 2 and simulacao[i].count(Tabuleiro.DESCONHECIDO) == 1:
                            passos_vitoria += 1
                        # Coluna
                        col = [simulacao[0][i], simulacao[1][i], simulacao[2][i]]
                        if col.count(self.tipo) == 2 and col.count(Tabuleiro.DESCONHECIDO) == 1:
                            passos_vitoria += 1
                    # Diagonais
                    diag1 = [simulacao[0][0], simulacao[1][1], simulacao[2][2]]
                    diag2 = [simulacao[0][2], simulacao[1][1], simulacao[2][0]]
                    if diag1.count(self.tipo) == 2 and diag1.count(Tabuleiro.DESCONHECIDO) == 1:
                        passos_vitoria += 1
                    if diag2.count(self.tipo) == 2 and diag2.count(Tabuleiro.DESCONHECIDO) == 1:
                        passos_vitoria += 1

                    if passos_vitoria >= 2:
                        return (l, c)

        
    def R3(self):
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

    def R4(self, oponente):
        #R4
        #(0, 0) > (2, 2)
        if self.matriz[0][0] == oponente and self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            return (2, 2)
        if self.matriz[2][2] == oponente and self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
            return (0, 0)

        # (0, 2) > (2, 0)
        if self.matriz[0][2] == oponente and self.matriz[2][0] == Tabuleiro.DESCONHECIDO:
            return (2, 0)
        if self.matriz[2][0] == oponente and self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
            return (0, 2)

    def R5(self):
        for l, c in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                return (l, c)

    def R6(self):
        lista = []
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))

        if lista:
            return lista[randint(0, len(lista) - 1)]
        return None
        
    def getJogada(self) -> (int, int):
        oponente = Tabuleiro.JOGADOR_X if self.tipo == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0

        # Regra 1
        jogada = self.R1(oponente)
        if jogada:
            return jogada

        # Regra 2
        jogada = self.R2()
        if jogada:
            return jogada

        # Regra 3
        jogada = self.R3()
        if jogada:
            return jogada

        # Regra 4
        jogada = self.R4(oponente)
        if jogada:
            return jogada

        # Regra 5
        jogada = self.R5()
        if jogada:
            return jogada

        # Regra 6
        jogada = self.R6()
        if jogada:
            return jogada

        return None
