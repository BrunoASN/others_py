a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))

delta= (b**2-4*a*c)

x=(-b+(delta**(1/2)))/(2*a)
y=(-b-(delta**(1/2)))/(2*a)

if(delta < 0):
	print("Não há soluções reais")
else:
	if (delta == 0):
		print("Há apenas uma solução e é x = ",x)
	else:
		print("Há duas soluções e são ",x," e ",y)