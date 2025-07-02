# -*- coding: utf-8 -*-

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)


    def getJogada(self) -> (int, int):
        lista = []
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))

        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            return lista[p]

from random import randint
def getJogada(self) -> (int, int):
    # Atalhos
    mat = self.matriz
    MEU = self.tipo
    OPONENTE = 1 if MEU == 4 else 4

    def linhas_colunas_diagonais():
        """Retorna todas as linhas, colunas e diagonais com suas posições."""
        posicoes = []
        # Linhas
        for i in range(3):
            posicoes.append([(i, j) for j in range(3)])
        # Colunas
        for j in range(3):
            posicoes.append([(i, j) for i in range(3)])
        # Diagonais
        posicoes.append([(i, i) for i in range(3)])
        posicoes.append([(i, 2-i) for i in range(3)])
        return posicoes

    def verificar_trinca(soma_alvo, jogador_tipo):
        for linha in linhas_colunas_diagonais():
            valores = [mat[l][c] for l, c in linha]
            if sum(valores) == soma_alvo and valores.count(0) == 1:
                for l, c in linha:
                    if mat[l][c] == 0:
                        return (l, c)
        return None

    # R1: Ganhar ou bloquear
    jogada = verificar_trinca(2 * MEU, MEU)  # Ganhar
    if jogada: return jogada
    jogada = verificar_trinca(2 * OPONENTE, OPONENTE)  # Bloquear
    if jogada: return jogada

    # R2: Jogada que cria dois caminhos de vitória
    for l in range(3):
        for c in range(3):
            if mat[l][c] == 0:
                mat[l][c] = MEU
                cont = 0
                for linha in linhas_colunas_diagonais():
                    valores = [mat[i][j] for i, j in linha]
                    if sum(valores) == MEU and valores.count(0) == 2:
                        cont += 1
                mat[l][c] = 0  # desfaz simulação
                if cont >= 2:
                    return (l, c)

    # R3: Centro
    if mat[1][1] == 0:
        return (1, 1)

    # R4: Canto oposto
    cantos = [(0,0), (0,2), (2,0), (2,2)]
    opostos = {(0,0):(2,2), (0,2):(2,0), (2,0):(0,2), (2,2):(0,0)}
    for canto in cantos:
        if mat[canto[0]][canto[1]] == OPONENTE:
            oposto = opostos[canto]
            if mat[oposto[0]][oposto[1]] == 0:
                return oposto

    # R5: Qualquer canto
    for canto in cantos:
        if mat[canto[0]][canto[1]] == 0:
            return canto

    # R6: Qualquer casa vazia
    for l in range(3):
        for c in range(3):
            if mat[l][c] == 0:
                return (l, c)

    return None  # Não há jogadas

