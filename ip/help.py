'''def fibo(n):
	if n <= 1:
		return n
	else:
		return fibo(n-1)+fibo(n-2)'''

'''def soma(n):
	if n == 1:
		return 1
	else:
		return n + soma(n-1)

print(soma(5))'''

'''def fat(n):
	if n == 0:
		return 0
	elif n == 1:
		return n
	else:
		return n*fat(n-1)

print(fat(5))'''

'''def multi(a,b):
	if a == 0 or b == 0:
		return 0
	elif a == 1:
		return b
	else:
		return a+multi(a,b-1)

print(multi(5,2))'''

'''def pot(a,b):
	if b == 0:
		return 1
	elif b == 1:
		return a
	else:
		return a+'''


'''str1 = input("String 1: ")
str2 = input("String 2: ")
print("Tamanho de {}: {} caracteres".format(str1, len(str1)))
print("Tamanho de {}: {} caracteres".format(str2, len(str2)))
if len(str1) == len(str2):
	print("As duas strings são de tamanhos iguais")
else:
	print("As duas strings são de tamanhos diferentes")
if str1 == str2:
	print("As duas strings são iguais")
else:
	print("As duas strings são diferentes")'''

'''string = str.lower(input("Frase: "))
vogal = 0
espaco = 0
for i in string:
	if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
		vogal += 1
	if i == " ":
		espaco += 1
print("Foram {} vogais e {} espaços.".format(vogal, espaco))'''



def pot(a,b):
	if b == 0:
		return 1
	elif b == 1:
		return a
	else:
		return a
