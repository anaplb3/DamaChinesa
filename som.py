#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import pygame
  
def creditos():
	for i in range(3):
		print("\t\t\t\t\t\t\tParabéns, você ganhou!")
		time.sleep(1)
		print("\n")
	print("\t\t\t\t\t\t\tAgora sobe os créditos produção!")
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
creditos()
