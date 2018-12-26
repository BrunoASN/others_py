def soma_elementos(lista):
	soma = 0
	for numero in lista:
		soma += numero
	return soma

lista = eval('[' + input("Digite sua lista: ") + ']')

lista = soma_elementos(lista)
print (lista)