def ganhouLocal1(peça,tabuleiro): #Ponta de cima
    contando = 0
    for i in range(4):
    	for j in tabuleiro[i]:
    		if [j] == peça:
        		contando += 1
    if contando == 10:
        return True
    else:
        return False

def ganhouLocal2(peça,tabuleiro): #Ponta de baixo
    contando = 0
    for i in range(4):
        for j in tabuleiro[i+13]:
            if [j] == peça:
                contando += 1
    if contando == 10:
        return True
    else:
        return False


def ganhouLocal3(peça,tabuleiro): #Primeira ponta do lado esquerdo
    elemento = 4
    contando1 = 0
    for i in range(4):
        for j in range(elemento):
            if tabuleiro[i+5][j] == peça:
                contando += 1
        elemento -= 1
    if contando == 10:
        return True
    else:
        return False


def ganhouLocal4(peça,tabuleiro): #Última ponta do lado direito
	elemento = 4
	contando = 0
	for i in range(4):
		for j in range(elemento):
			if tabuleiro[i+5][-j-1] == peça:
				contando += 1
		elemento -= 1
	if contando == 10:
		return True
	else:
		return False


def ganhouLocal5(peça,tabuleiro): #Primeira ponta do lado esquerdo
    elemento = 1
    contando = 0
    for i in range(4):
        for j in range(elemento):
        	if tabuleiro[i][j] == peça:
        		contando += 1
        elemento += 1
    if contando == 10:
        return True
    else:
        return False


def ganhouLocal6(peça, tabuleiro): #Última ponta do lado direito
    elemento = 1
    contando = 0
    for i in range(4):
        for j in range(elemento):
            if tabuleiro[i][-j-1] == peça:
                contando += 1
        elemento += 1
    if contando == 10:
        return True
    else:
        return False

def chamarGanhador(numJogador, pecas, tabuleiro):
	if numJogador == 2:
		def verificaDois(pecas,tabuleiro):
			jogador1 = ganhouLocal2(pecas[0], tabuleiro)
			jogador2 = ganhouLocal1(pecas[1], tabuleiro)
			if jogador1 == True or jogador2 == True:
				return True
			else:
				return False
		return verificaDois(pecas, tabuleiro)
	elif numJogador == 3:
		def verificaTres(pecas, tabuleiro):
			jogador1 = ganhouLocal6(pecas[0], tabuleiro)
			jogador2 = ganhouLocal1(pecas[1], tabuleiro)
			jogador3 = ganhouLocal5(pecas[2], tabuleiro)
			if jogador1 == True or jogador2 == True or jogador3 == True:
				return True
			else:
				return False
		return verificaTres(pecas, tabuleiro)
	elif numJogador == 4:
		def verificaQuatro(pecas, tabuleiro):
			jogador1 = ganhouLocal6(pecas[0], tabuleiro)
			jogador2 = ganhouLocal5(pecas[1], tabuleiro)
			jogador3 = ganhouLocal4(pecas[2], tabuleiro)
			jogador4 = ganhouLocal3(pecas[3], tabuleiro)
			if jogador1 == True or jogador2 == True or jogador3 == True or jogador4 == True:
				return True
			else:
				return False
		return verificaQuatro(pecas, tabuleiro)
	else:
		def verificaSeis(pecas, tabuleiro):
			jogador1 = ganhouLocal2(peca[0], tabuleiro)
			jogador2 = ganhouLocal1(peca[1], tabuleiro)
			jogador3 = ganhoulocal6(peca[2], tabuleiro)
			jogador4 = ganhouLocal5(peca[3], tabuleiro)
			jogador5 = ganhouLocal4(peca[4], tabuleiro)
			jogador6 = ganhouLocal3(peca[5], tabuleiro)
			if jogador1 == True or jogador2 == True or jogador3 == True or jogador4 == True or jogador5 == True or jogador6 == True:
				return True
			else:
				return False
		return verificaSeis(pecas, tabuleiro)