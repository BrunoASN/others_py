coluna = int(input("digite a largura: "))
linha = int(input("digite a altura: "))
x = coluna
y = linha

while (linha > 0):
	while (coluna > 0):
		if(linha == 1 or coluna == 1 or linha == y or coluna == x):
			print ("#", end = "")
		else:
			print (" ", end = "")
		coluna = coluna - 1
	linha = linha - 1
	print ()
	coluna = x