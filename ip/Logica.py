import GUI
import LogicaMovimento

def pecaDoJogador(numJogadores):
  pecas = []
  if numJogadores == 2:
    pecas = ["N", "V"]
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

  while(venceu==False):
    for i in nomes:
      print("Movimentos: 'r' = direita, 'l' = esquerda, 'ur' = para cima e direita, 'ul' = para cima e esquerda, 'dr' = para baixo e direita, 'dl' para baixo e esquerda")
      movimento = input("{}, agora é a sua vez: ".format(i).split("-"))
      
      linha = int(movimento[0])
      posicaoNaLinha = int(movimento[1])
      direcao = movimento[2]
      salto = False
      x = LogicaMovimento.pegarProximaPosicao(linha-1, posicaoNaLinha-1, direcao,salto)
      linhaDestino = x[0]
      colunaDestino = x[1]
      moverPeca(tabuleiro, linha-1, posicaoNaLinha-1, linhaDestino-1, colunaDestino-1)
      GUI.imprimirTabuleiro(tabuleiro)




def moverPeca(tabuleiro, linha, posicaoNaLinha, linhaDestino, colunaDestino):
  tabuleiro[linhaDestino][colunaDestino] = tabuleiro[linha][posicaoNaLinha]
  tabuleiro[linha][posicaoNaLinha] = "O"

def tentarMovimento(movimento, tabuleiro, jogador, salto = False):
  linha = movimento[0]
  coluna = movimento[1]
  direcao = movimento[2]

  
  #verificar se a peça esta dentro do tabuleiro
  #verificar se a posição para mover é vazia
  #pegar proxima posição e verificar se a posição destino é vazia(sem salto)
  #se der erro tentar com salto
  #se ok, verificar se o tamanho de movimento é 3, para encerrar
  #usar recursividade para o metodo do salto (salto composto)(mudar salto para true, mudar a linha,coluna para a linha e coluna de destino atual)
  # remover a direção já destada (del movimento 2)

'''def estahDentroDoTabuleiro(linhaInicial, colunaInicial, tabuleiro):
  #se linhainicial >= 1 e linhaInicial <= len(tabuleiro)
    #se colunaInicial >=1 e colunaInicial <= len(tabuleiro[linha])'''
