#================================================================ 
# EL factorial de un número entero positivo
# es el producto de todos los enteros positivo
# desde 1 hasta él
# Ej: 5! = 1*2*3*4*5
#===============================================================
import math

# Enfoque iterativo ascendente
def factorial_asc(n):
	fact = 1
	for num in range(2, n+1):
		fact *= num
	return fact

# Enfoque iterativo descendente
def factorial_desc(n):
	fact = 1
	for num in range(n, 1, -1):
		fact *= num
	return fact

# Enfoque recursivo
def factorial_recursivo(n):
	if n < 2:
		return 1
	else:
		return n * factorial_recursivo(n-1)

def main():
	print(factorial_asc(3))
	print(factorial_desc(3))
	print(factorial_recursivo(5))
	print(math.factorial(5))


main()