from miller_rabin import *
from gcd import *

def generate_large_prime(keysize):
	while True:
		num = (dice.randrange(1 << keysize - 1, 1 << keysize) << 1) + 1 # odd number
		if miller_rabin(num):	
			return num

def is_coprime(a, b):
	return gcd(a, b) == 1

# Extended Euclidean Algorithm
def modular_inverse(a, b):
	r0 = b; r1 = a
	x1 = 0; x0 = 1
	y1 = 1; y0 = 0

	
	while r0 != 0:
		q = r1 // r0
		r1, r0 = r0, r1 - q * r0
		x0, x1 = x1, x0 - q * x1
		y0, y1 = y1, y0 - q * y1

	if x0 < 0:
		x0 += b

	return x0

def keygen(keysize = 1024):
	e = d = N = 0

	p = generate_large_prime(keysize)
	q = generate_large_prime(keysize)

	print(f"p = {p}")
	print(f"q = {q}")

	N = p*q
	phiN = (p - 1)*(q - 1)

	# while True:
	# 	e = dice.randrange(1 << keysize - 1, 1 << keysize)
	# 	if is_coprime(e, phiN):
	# 		break
	e = 65537
	d = modular_inverse(e, phiN)

	return e, d, N


