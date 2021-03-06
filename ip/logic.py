import GUI
import LogicaGabarito

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
        venceu = verificaDois(pecas, numJogadores, tabuleiro)
    except IndexError:
      print("Ops, posições inválidas... Tente de novo!")
      GUI.imprimirTabuleiro(tabuleiro)

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

'''def verificaSeGanhou(peça, quantidadedejogador, tabuleiro):
    if quantidadedejogador == 2:
        def ganhouLocal1(peça):
          for i in range(4):
            for j in tabuleiro[i]:
              if [j] != letra:
                    return False
                    break
        return True

        def ganhouLocal2(letra):
            for i in range(4):
                for j in tabuleiro[i+14]:
                    if [j] != letra:
                        return False
                        break
        return True

    elif quantidadedejogador == 3:
        def ganhouLocal3(letra):
            elemento = 4
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i+5][j] != letra:
                        return False
                        break
                elemento -= 1
            return True

        def ganhouLocal4(letra):
            elemento = 4
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i+5][-j-1] != letra:
                        return False
                elemento -= 1
            return True

        def ganhouLocal2(letra):
            for i in range(4):
                for j in tabuleiro[i+14]:
                    if [j] != letra:
                        return False
    elif quantidadedejogador == 4:
        def ganhouLocal3(letra):
            elemento = 4
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i+5][j] != letra:
                        return False
                elemento -= 1
            return True

        def ganhouLocal4(letra):
            elemento = 4
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i+5][-j-1] != letra:
                        return False
                elemento -= 1
            return True

        def ganhouLocal5(letra):
            elemento = 1
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i][j] != letra:
                        return False
                elemento += 1
            return True

        def ganhouLocal6(letra):
                elemento = 1
                for i in range(4):
                    for j in range(elemento):
                        if tabuleiro[i][-j-1] != letra:
                            return False
                    elemento += 1
                return True

    elif quantidadedejogador == 6:
        def ganhouLocal1(letra):
          for i in range(4):
            for j in tabuleiro[i]:
              if [j] != letra:
                    return False
        return True

        def ganhouLocal2(letra):
            for i in range(4):
                for j in tabuleiro[i+14]:
                    if [j] != letra:
                        return False
                        break
        def ganhouLocal3(letra):
            elemento = 4
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i+5][j] != letra:
                        return False
                elemento -= 1
            return True

        def ganhouLocal4(letra):
            elemento = 4
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i+5][-j-1] != letra:
                        return False
                elemento -= 1
            return True

        def ganhouLocal5(letra):
            elemento = 1
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i][j] != letra:
                        return False
                elemento += 1
            return True

        def ganhouLocal6(letra):
                elemento = 1
                for i in range(4):
                    for j in range(elemento):
                        if tabuleiro[i][-j-1] != letra:
                            return False
                    elemento += 1
                return True'''