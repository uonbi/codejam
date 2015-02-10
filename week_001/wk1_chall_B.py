#!/usr/bin/python3
"""
Author: Denis Karanja,
Lead, Sci Code Jam (codejam.sci.website)
Task: Divisibility sum
Status:...COMPLETED
"""

def is_prime(num):
	'''Check if a number is prime'''
	if num is 1: return False
	if num % 2 is 0: return (num == 2)
	start = 3
	while (start**2) <= num:
		if num % start is 0:
			return False
		start += 2
	return True

def get_primes(limit, primes = []):
	'''Return all primes below limit'''
	for x in range(3, limit):
		if is_prime(x):
			primes.append(x)
	return primes

def is_odd(number):
	'''Check if a number is odd'''
	if number % 2 is 0:
		return False
	return True

def main():
	prime_sum, flag, array = 0, 0, []
	primes = get_primes(10)
	prime_len = len(primes)

	#iterrate thru all numbers
	for x in range(1, 100000):
		for prime in primes:
			if x % prime is 0:
				flag += 1
		
		#check if the flag val is equivalent to the length of primes
		#and that the value of x is odd 
		if flag is prime_len and is_odd(x):
			prime_sum += x
			#print (x)
		
		#reset flag
		flag = 0

	return prime_sum


if __name__ == "__main__":
	print(main())