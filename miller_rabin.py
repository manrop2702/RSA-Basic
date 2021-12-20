import random

dice = random.SystemRandom()

def single_test(n, a):
	exp = n - 1
	while not exp & 1: 	
		exp >>= 1

	if pow(a, exp, n) == 1:	# a^exp = 1 (mod n)
		return True

	while exp < n - 1:
		if pow(a, exp, n) == n - 1:
			return True
		exp <<= 1

	return False

def miller_rabin(n, k = 40):	# k -> the number of times you want to do the test
	for i in range(k):
		a = dice.randrange(2, n - 1)	# 1 < a < n - 1
		if not single_test(n, a):
			return False
	return True
