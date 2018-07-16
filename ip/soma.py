def soma(n):
	if n == 0:
		return n
	else:
		return n+soma(n-1)

print(soma(5))