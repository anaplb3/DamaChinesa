import GUI
import LogicaGabarito

def pecaDoJogador(numJogadores):
  pecas = []
  if numJogadores == 2:
    pecas = ["R", "V"]
  elif numJogadores == 3:
    pecas = ["R", "B", "A"]
  elif numJogadores == 4:
    pecas = ["N", "C", "B", "A"]
  else:
    pecas = ["R", "N", "C", "B", "A", "V"]
  return pecas

def parteUm(tabuleiro):
     for linha in range(4):
         for coluna in range(len(tabuleiro[linha])):
             tabuleiro[linha][coluna] = "R"

def parteDois(tabuleiro):
     cont=4
     for linha in range(4,8,1):
          for coluna in range(cont):
               tabuleiro[linha][coluna] = "N"
          cont -= 1

     colunas = 4
     for linha in range(4,8,1):
          for coluna in range(9,9 + colunas):
               tabuleiro[linha][coluna] = "C"
          colunas -= 1


def parteTres(tabuleiro):
     cont = 1
     for linha in range(9,13,1):
          for coluna in range(cont):
               tabuleiro[linha][coluna] = "B"
          cont += 1
     
     colunas = 9
     for linha in range(8,13,1):
          for coluna in range(9, colunas): 
               tabuleiro[linha][coluna] = "A"
          colunas += 1
               
def parteQuatro(tabuleiro):    
  for linha in range(13,17,1):
        for coluna in range(len(tabuleiro[linha])):
            tabuleiro[linha][coluna] = "V"

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
  venceu = False
  adicionarPecas(tabuleiro, numJogadores)
  pecas = pecaDoJogador(numJogadores)

  while(venceu==False):
    try:
      for nome in range(len(nomes)):
        print("Movimentos: 'r' = direita, 'l' = esquerda, 'ur' = para cima e direita, 'ul' = para cima e esquerda, 'dr' = para baixo e direita, 'dl' para baixo e esquerda")
        movimento = input("{}, agora é a sua vez de mexer a peça {}: ".format(nomes[nome], pecas[nome])).split("-")
        linha = int(movimento[0])
        posicaoNaLinha = int(movimento[1])
        direcao = str.lower(movimento[2])
        if erros(tabuleiro, movimento, linha-1, posicaoNaLinha-1, nome, pecas) == False:
          print("\n")
          print("Ops, direção ou movimento errado! Tente de novo.")
          GUI.imprimirTabuleiro(tabuleiro)
          movimento = input("{}, agora é a sua vez de mexer a peça {}: ".format(nomes[nome], pecas[nome])).split("-")
          linha = int(movimento[0])
          posicaoNaLinha = int(movimento[1])
          direcao = str.lower(movimento[2])
        saltoComposto(tabuleiro, linha, posicaoNaLinha, direcao, movimento)
        GUI.imprimirTabuleiro(tabuleiro)
    except IndexError:
      print("Ops, posições inválidas... Tente de novo!")
      GUI.imprimirTabuleiro(tabuleiro)
      jogar(numJogadores, tabuleiro, nomes)


def erros(tabuleiro, movimento, linha, posicaoNaLinha, nomes, pecas):
  if valindandoDireção(movimento) == False or validandoPeca(tabuleiro, linha, posicaoNaLinha, nomes, pecas) == False:
    return False
  else:
    return True

def moverPeca(tabuleiro, linha, posicaoNaLinha, linhaDestino, colunaDestino):
  tabuleiro[linhaDestino][colunaDestino] = tabuleiro[linha-1][posicaoNaLinha-1]
  tabuleiro[linha-1][posicaoNaLinha-1] = "O"

def lugarVazio(tabuleiro, linhaDestino, colunaDestino):
  if tabuleiro[linhaDestino][colunaDestino] == "O":
    return True
  else:
    return False

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
      jump = salto(tabuleiro, linhaA, posicaoNaLinhaA, direcao)
      linhaA = jump[0]
      posicaoNaLinhaA = jump[1]
      direcao = i
    linhaDestino = jump[0]-1
    print(linhaDestino)
    colunaDestino = jump[1]-1
    print(posicaoNaLinha)  
    moverPeca(tabuleiro, linha, posicaoNaLinha, linhaDestino,colunaDestino) 
  else:
    jump = salto(tabuleiro, linha, posicaoNaLinha, direcao)
    linhaDestino = jump[0]-1
    colunaDestino = jump[1]-1
    moverPeca(tabuleiro, linha, posicaoNaLinha, linhaDestino, colunaDestino)
    
def valindandoDireção(movimento):
  for i in movimento[2:]:
    if i != "r" and i != "l" and i != "ur" and i != "ul" and i != "dl" and i != "dr":
      return False
    else:
      return True 

def validandoPeca(tabuleiro, linha, posicaoNaLinha, nome, pecas):
    if tabuleiro[linha][posicaoNaLinha] != pecas[nome]:
      return False
    else:
      return True