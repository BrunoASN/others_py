def primo(k):
	if ( k%2 != 0  and k%3 != 0 and k%5 != 0 and k%7 != 0 or k == 2 or k == 3 or k == 5 or k == 7 ):
		return k

def maior_primo(n):
	if (primo(n) == n):
		return n
	else:
		k = n
		while (primo(k) != k):
			k = k - 1
			if (primo(k) == k):
				return k