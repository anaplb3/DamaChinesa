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
      GUI.imprimirTabuleiro(tabuleiro)
      for nome in range(len(nomes)):
        print("Movimentos: 'r' = direita, 'l' = esquerda, 'ur' = para cima e direita, 'ul' = para cima e esquerda, 'dr' = para baixo e direita, 'dl' para baixo e esquerda")
        movimento = input("{}, agora é a sua vez de mexer a peça {}: ".format(nomes[nome], pecas[nome])).split("-")
        print("\n\n")
        movimentacao(movimento, tabuleiro)
        GUI.imprimirTabuleiro(tabuleiro)
        print("\n\n")
    except IndexError:
      print("Ops, posições inválidas... Tente de novo!")
      jogar(numJogadores, tabuleiro, nomes)

def chamarProxima(linha, posicaoNaLinha, direcao, salto):
  posicao = LogicaGabarito.pegarProximaPosicao(linha, posicaoNaLinha,direcao,salto)
  return posicao

def moverPeca(tabuleiro, linha, posicaoNaLinha, linhaDestino, colunaDestino):
  tabuleiro[linhaDestino][colunaDestino] = tabuleiro[linha-1][posicaoNaLinha-1]
  tabuleiro[linha-1][posicaoNaLinha-1] = "O"

def salto(tabuleiro, linha, posicaoNaLinha, direcao, linhaDestino, colunaDestino):
  if tabuleiro[linhaDestino][colunaDestino] != "O":
    x = LogicaGabarito.pegarProximaPosicao(linha, posicaoNaLinha, direcao,salto=True)
    linhaDestino = x[0]-1
    colunaDestino = x[1]-1
    moverPeca(tabuleiro, linha, posicaoNaLinha, linhaDestino, colunaDestino)
  else:
    moverPeca(tabuleiro, linha, posicaoNaLinha, linhaDestino, colunaDestino)


def movimentacao(movimento, tabuleiro):
  if len(movimento) == 3:
    linha = int(movimento[0])
    posicaoNaLinha == int(movimento[1])
    direcao = movimento[2]
    proximo = LogicaGabarito.pegarProximaPosicao(linha, posicaoNaLinha, direcao, salto)
    linhaDestino = proximo[0]-1
    colunaDestino = proximo[1]-1
    salto(tabuleiro, linha, posicaoNaLinha, direcao, linhaDestino, colunaDestino)
  
  '''for i in movimento[2:]:
    direcao =


def movimentos(tabuleiro, movimento):

def movimentacao(movimento, tabuleiro, linhaDestino, colunaDestino):
  if len(movimento) > 3:
    for i in movimento[2:]:
      linha = int(movimento[0])
      posicaoNaLinha = int(movimento[1])
      direcao = i
      salto(tabuleiro, linha, posicaoNaLinha, direcao, linhaDestino, colunaDestino)
  else:
    linha = int(movimento[0])
    posicaoNaLinha = int(movimento[1])
    direcao = movimento[2]
    x = LogicaGabarito.pegarProximaPosicao(linha, posicaoNaLinha, direcao, salto=False)
    linhaDestino = x[0]-1
    colunaDestino = x[1]-1
    salto(tabuleiro, linha, posicaoNaLinha, direcao, linhaDestino, colunaDestino)'''