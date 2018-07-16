#coding: utf-8

import GUI
import logic


listaNomes = []
numJogadores = GUI.menuInicial()
listaNomes = GUI.nomes(numJogadores)
tabuleiro = GUI.criarTabuleiro()
adicionarPecas = logic.adicionarPecas(tabuleiro,numJogadores)

jogo = logic.jogar(numJogadores, tabuleiro, listaNomes)


