#!/usr/bin/python
# -*- coding: utf-8 -*-
import GUI
import LogicaGabarito
from ganhador import *
import time
import pygame

def pecaDoJogador(numJogadores):
  pecas = []
  if numJogadores == 2:
    pecas = ['\033[31m'+'R'+'\033[0;0m', '\033[37m'+'V'+'\033[0;0m']
  elif numJogadores == 3:
    pecas = ['\033[31m'+'R'+'\033[0;0m', '\033[34m'+'B'+'\033[0;0m', '\033[36m'+'A'+'\033[0;0m']
  elif numJogadores == 4:
    pecas = ['\033[35m'+'N'+'\033[0;0m', '\033[33m'+'C'+'\033[0;0m', '\033[34m'+'B'+'\033[0;0m', '\033[36m'+'A'+'\033[0;0m']
  else:
    pecas = ['\033[31m'+'R'+'\033[0;0m', '\033[35m'+'N'+'\033[0;0m', '\033[33m'+'C'+'\033[0;0m', '\033[34m'+'B'+'\033[0;0m', '\033[36m'+'A'+'\033[0;0m', '\033[37m'+'V'+'\033[0;0m']
  return pecas

def parteUm(tabuleiro):
     for linha in range(4):
         for coluna in range(len(tabuleiro[linha])):
             tabuleiro[linha][coluna] = '\033[31m'+'R'+'\033[0;0m'

def parteDois(tabuleiro):
     cont=4
     for linha in range(4,8,1):
          for coluna in range(cont):
               tabuleiro[linha][coluna] = '\033[35m'+'N'+'\033[0;0m'
          cont -= 1

     colunas = 4
     for linha in range(4,8,1):
          for coluna in range(9,9 + colunas):
               tabuleiro[linha][coluna] = '\033[33m'+'C'+'\033[0;0m'
          colunas -= 1


def parteTres(tabuleiro):
     cont = 1
     for linha in range(9,13,1):
          for coluna in range(cont):
               tabuleiro[linha][coluna] = '\033[34m'+'B'+'\033[0;0m'
          cont += 1
     
     colunas = 9
     for linha in range(8,13,1):
          for coluna in range(9, colunas): 
               tabuleiro[linha][coluna] = '\033[36m'+'A'+'\033[0;0m'
          colunas += 1
               
def parteQuatro(tabuleiro):    
  for linha in range(13,17,1):
        for coluna in range(len(tabuleiro[linha])):
            tabuleiro[linha][coluna] = '\033[37m'+'V'+'\033[0;0m'

def adicionarPecas(tabuleiro, numJogadores):
  if numJogadores == 2:
      parteUm(tabuleiro)
      parteQuatro(tabuleiro)


  elif numJogadores == 3:
      parteUm(tabuleiro)
      parteTres(tabuleiro)

  elif numJogadores == 4:
      parteDois(tabuleiro)
      parteTres(tabuleiro)

  else:
      parteUm(tabuleiro)
      parteDois(tabuleiro)
      parteTres(tabuleiro)
      parteQuatro(tabuleiro)


def jogar(numJogadores, tabuleiro, nomes):
  adicionarPecas(tabuleiro, numJogadores)
  pecas = pecaDoJogador(numJogadores)
  venceu = True

  while(venceu==False):
    try:
      for nome in range(len(nomes)):
        print("\n")
        print("Movimentos: 'r' = direita, 'l' = esquerda, 'ur' = para cima e direita, 'ul' = para cima e esquerda, 'dr' = para baixo e direita, 'dl' para baixo e esquerda")
        movimento = input("{}, agora é a sua vez de mexer a peça {}: ".format(nomes[nome], pecas[nome])).split("-")
        linha = int(movimento[0])
        posicaoNaLinha = int(movimento[1])
        direcao = str.lower(movimento[2])
        if validandoPeca(tabuleiro, linha, posicaoNaLinha, nome, pecas) == False or pertenceAoTabuleiro(linha, posicaoNaLinha) == False:
          GUI.limparTela()
          print("\t\t\t\t\t\t\t\tOpa, não dá pra fazer esse movimento! Tente de novo!")
          print("\n")
          GUI.imprimirTabuleiro(tabuleiro)
          print("\n")
          movimento = input("{}, agora é a sua vez de mexer a peça {}: ".format(nomes[nome], pecas[nome])).split("-")
          linha = int(movimento[0])
          posicaoNaLinha = int(movimento[1])
          direcao = str.lower(movimento[2])
        GUI.limparTela()
        saltoComposto(tabuleiro, linha, posicaoNaLinha, direcao, movimento)
        GUI.imprimirTabuleiro(tabuleiro)
        venceu = chamarGanhador(numJogadores,pecas,tabuleiro)
    except Exception:
      GUI.limparTela()
      print("\t\t\t\t\t\t\t\tOps, movimento inválido... Tente de novo!")
      print("\n")
      GUI.imprimirTabuleiro(tabuleiro)
      print("\n")
  print("\n")
  creditos()


def moverPeca(tabuleiro, linha, posicaoNaLinha, linhaDestino, colunaDestino):
  tabuleiro[linhaDestino][colunaDestino] = tabuleiro[linha-1][posicaoNaLinha-1]
  tabuleiro[linha-1][posicaoNaLinha-1] = "O"

def lugarVazio(tabuleiro, linhaDestino, colunaDestino):
  if tabuleiro[linhaDestino][colunaDestino] == "O":
    return True
  else:
    return False

def validandoPeca(tabuleiro, linha, posicaoNaLinha, nome, pecas):
    if tabuleiro[linha-1][posicaoNaLinha-1] != pecas[nome]:
      return False
    else:
      return True

def salto(tabuleiro, linha, posicaoNaLinha, direcao):
  linha=int(linha)
  posicaoNaLinha = int(posicaoNaLinha)
  testeJogo = LogicaGabarito.pegarProximaPosicao(linha, posicaoNaLinha, direcao, salto=False)
  linhaDestino = testeJogo[0]-1
  colunaDestino = testeJogo[1]-1
  if lugarVazio(tabuleiro, linhaDestino, colunaDestino) == True:
    return testeJogo
  else:
    novoMovimento = LogicaGabarito.pegarProximaPosicao(linha, posicaoNaLinha, direcao,salto=True)
    return novoMovimento


def saltoComposto(tabuleiro, linha, posicaoNaLinha, direcao, movimento):
  linhaA=int(linha)
  posicaoNaLinhaA = int(posicaoNaLinha)
  if len(movimento) > 3:
    for i in movimento[2:]:
      direcao = i
      jump = salto(tabuleiro, linhaA, posicaoNaLinhaA, direcao)
      linhaA = jump[0]
      posicaoNaLinhaA = jump[1]
      linhaDestino = jump[0]-1
    colunaDestino = jump[1]-1 
    moverPeca(tabuleiro, linha, posicaoNaLinha, linhaDestino,colunaDestino) 
  else:
    jump = salto(tabuleiro, linha, posicaoNaLinha, direcao)
    linhaDestino = jump[0]-1
    colunaDestino = jump[1]-1
    moverPeca(tabuleiro, linha, posicaoNaLinha, linhaDestino, colunaDestino)

def creditos():
  for i in range(3):
    print("\t\t\t\t\t\t\t\tParabéns, você ganhou!")
    time.sleep(1)
    print("\n")
  print("\n")
  print("\t\t\t\t\t\t\t\tAgora sobe os créditos, produção!")
  print("\n")
  pygame.init()
  pygame.mixer.music.load("chi.mp3")
  pygame.mixer.music.play()
  lista = ["Damas Chinesas", "*"*50,"Desenvolvido por:", "*"*50, "Ana Paula Lima", "*"*50, "Isabela Hélebe", "*"*50, "Ana Karolynne", "*"*50, "Projeto de Introdução a Programação", "*"*50,"Ministrado por Eduardo Falcão", "*"*50,"Obrigada e até a próxima!", "*"*50]
  for i, v in enumerate(lista):
    if i%2 == 0:
      time.sleep(1)
      print("\t\t\t\t\t\t\t{}".format(v))
    else:
      time.sleep(1)
      print("\t\t\t\t\t\t{}".format(v))

def pertenceAoTabuleiro(linha,coluna):
  linha=(int(linha)-1)
  coluna= (int(coluna)-1)

  if linha >= 0 and linha <= 3:
    if (linha == 0 and coluna == 0) or (linha == 1 and (coluna == 0 or coluna == 1)) or (linha == 2 and (coluna >= 0 and coluna <= 2)) or (linha == 3 and (coluna >= 0 and coluna <= 3)):
        return True
    else:
        return False
  elif linha >=4 and linha <= 7:
    if linha == 4 and (coluna >= 0 and coluna <= 12) or (linha == 5 and (coluna >= 0 and coluna <= 11)) or (linha == 6 and (coluna >= 0 and coluna <= 10)) or (linha == 7 and (coluna >= 0 and coluna <= 9)):
        return True
    else:
        return False   
  elif linha >= 8 and linha <= 12:
    if linha == 8 and (coluna >= 0 and coluna <= 8) or linha == 9 and (coluna >= 0 and coluna <= 9) or linha == 10 and (coluna >= 0 and coluna <= 10) or linha == 11 and (coluna >= 0 and coluna <= 11) or linha == 12 and (coluna >= 0 and coluna <= 12):
        return True
    else: 
        return False
  elif linha >= 13 and linha <= 16:
    if linha == 13 and (coluna >= 0 and coluna <= 3) or linha == 14 and (coluna >= 0 and coluna <= 2) or linha == 15 and (coluna >= 0 and coluna <= 1) or linha == 16 and coluna == 0:
        return True
    else:
        return False
  else:
      return False