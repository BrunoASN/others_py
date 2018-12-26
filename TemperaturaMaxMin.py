def MinMax (temperaturas):
	print ("Temperatura mínima: ", minima(temperaturas))
	print ("Temperatura máxima: ", maxima(temperaturas))
	
def minima(temps):
	min = temps[0]
	i = 1
	while i < len(temps):
		if temps[i]<min:
			min = temps[i]
		i = i + 1
	return min
	
def maxima(temps):
	max = temps[0]
	i = 1
	while i < len(temps):
		if temps[i]>max:
			max = temps[i]
		i = i + 1
	return max
	
temperaturas = eval('[' + input("Digite sua lista de temperaturas: ") + ']')
MinMax(temperaturas)