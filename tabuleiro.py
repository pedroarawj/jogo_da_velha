# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        # Linhas
        for l in range(3):
            soma = 0
            for c in range(3):
                soma += self.matriz[l][c]
            if soma == 3:
                return Tabuleiro.JOGADOR_0
            if soma == 12:
                return Tabuleiro.JOGADOR_X

        # Colunas
        for c in range(3):
            soma = self.matriz[0][c] + self.matriz[1][c] + self.matriz[2][c]
            if soma == 3:
                return Tabuleiro.JOGADOR_0
            if soma == 12:
                return Tabuleiro.JOGADOR_X

        # Diagonal principal
        soma = self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2]
        if soma == 3:
            return Tabuleiro.JOGADOR_0
        if soma == 12:
            return Tabuleiro.JOGADOR_X

        # Diagonal secundária
        soma = self.matriz[0][2] + self.matriz[1][1] + self.matriz[2][0]
        if soma == 3:
            return Tabuleiro.JOGADOR_0
        if soma == 12:
            return Tabuleiro.JOGADOR_X

        return Tabuleiro.DESCONHECIDO
