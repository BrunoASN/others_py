def FatorarEPrimo(n):
	fator = 2
	multiplicidade = 0
	cont = 0

	while (n > 1):
		while (n % fator == 0):
			multiplicidade = multiplicidade + 1
			n = n/fator
			cont = cont + 1
		if (multiplicidade > 0):
			print (fator, "^", multiplicidade)
		fator = fator + 1
		multiplicidade = 0
	if (cont == 1):
		print ("O numero é primo.")
	else:
		print ("O numero não é primo.")
		
		
n = int(input("\nDigite um numero maior que zero: \n"))
if (n>0):
	FatorarEPrimo(n)
else:
	while (n<=0):	
		print ("Valor inválido, vamos tentar novamente.")
		n = int(input("\nDigite um numero maior que zero: \n"))
	FatorarEPrimo(n)