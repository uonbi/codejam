#!/usr/bin/python3
"""
Author: Denis Karanja,
Lead, Sci Code Jam (codejam.sci.website)
Task: Product of factorials of highest powers
Status:...COMPLETED
"""
import math

def scibigpow(limit, base_limit):
	'''Finds the highest power of numbers that
	give a result <= limit'''
	assert type(limit) is int

	power, product = 2, 1
	number = 2

	while number <= base_limit:
		result = number ** power

		if result > limit:
			power -= 1
			product *= math.factorial(power)
			number += 1
			power = 2
		else:
			power += 1

	return (str(product)[49:70])#50th to the 70th numbers
		
		

def is_prime(num):
	'''Checks if a number is prime'''
	assert type(num) is int
	assert num > 0
	if num is 1: return False
	if num % 2 is 0: return (num == 2)
	start = 3

	while (start ** 2) <= num:
		if num % start is 0:
			return False
		start += 2
	return True
			

def largest_prime(limit):
	'''Returns the largest prime below the limit'''
	i = limit - 1
	while not is_prime(i):
		i -= 1
	return i

def main():
	bigpow_prod = scibigpow(largest_prime(2000000000), 999)

	return (bigpow_prod)

if __name__ == "__main__":
	print(main())



