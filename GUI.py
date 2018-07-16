#coding: utf-8
import time

def menuInicial():
    try:
        print("\t\t\t\t******************************************************************************************************************* \n"
              "\t\t\t\t*****************************************        DAMAS       ****************************************************** \n"
              "\t\t\t\t*****************************************       CHINESAS     ****************************************************** \n"
              "\t\t\t\t******************************************************************************************************************* \n")
        
        tabuleiro = criarTabuleiro()
        imprimirTabuleiro(tabuleiro)
        print("\n")
        numJogadores = input("Quantos jogadores? ")
        if numJogadores.isdigit() == False or int(numJogadores) <= 1 or int(numJogadores) == 5 or int(numJogadores) >= 7:
            print('\n')
            print("Opa, número de jogadores inválido... Tente de novo!")
            print("\n")
            return menuInicial()
        else:
            return int(numJogadores) 
    except KeyboardInterrupt:
        print("\n")
        print("\t\t\t\t\t\t\t\t\tOkay, até mais!")
        exit()

          

def limparTela():
    print("\n"*50)

def nomes(numJogadores):
    try:
        nomes = []
        for i in range(numJogadores):
            nomes.append(input("Qual seu nome, jogador {}? ".format(i+1)))
        return nomes
    except KeyboardInterrupt:
        print("Okay, até mais!")
        exit()


def criarTabuleiro():
    tabuleiro = []
    for linha in range(4):
        tabuleiro.append([])
        for coluna in range(linha+1):
            tabuleiro[linha].append("O")
    tamanho = 13   
    for linha in range(4,8,1):
        tabuleiro.append([])
        for coluna in range(tamanho):
            tabuleiro[linha].append("O")
        tamanho -=1
        
    for linha in range(8,13,1):
        tabuleiro.append([])
        for coluna in range(linha + 1 ):
            tabuleiro[linha].append("O")
            
    tamanho = 4
    for linha in range(13,17,1):
        tabuleiro.append([])
        for coluna in range(tamanho):
            tabuleiro[linha].append("O")
        tamanho -=1

            
    return tabuleiro

def imprimirLinhaComEspaco(tabuleiro, linha, espaco):
    espacamento = " " * espaco
    print(espacamento, end = "")
    for i in tabuleiro[linha]:
        print(i + " ", end = "")
    print()
     
    

def imprimirTabuleiro(tabuleiro):
    espaco1 = 15
    espaco2 = 3
    espaco3 = 5
    espaco4 = 11
    numero = 1

    for linha in range(4):
        print(70* " ", numero, end="")
        imprimirLinhaComEspaco(tabuleiro,linha,espaco1)
        espaco1 -= 1
        numero += 1
    for linha in range(4,9,1):
        print(70* " ", numero, end="")
        imprimirLinhaComEspaco(tabuleiro,linha,espaco2)
        espaco2 +=1
        numero += 1
    for linha in range(9,13):
        print(70* " ", numero,end="")
        imprimirLinhaComEspaco(tabuleiro,linha,espaco3)
        espaco3 -=1
        numero += 1
    for linha in range(13,17):
        print(70* " ", numero, end="")
        imprimirLinhaComEspaco(tabuleiro,linha,espaco4)
        espaco4 +=1
        numero += 1

    return tabuleiro

    
    
        
        
    
    
    
    
        
    
        
            
