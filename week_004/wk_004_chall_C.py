#!/usr/bin/python3
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics,
Email: dee.caranja@gmail.com,
(Largest Pandigital prime)
Status.. COMPLETED...
"""
import itertools, time
def is_prime(num):
	'''
	Check if a number is prime
	@param int
	@return boolean
	'''
	if num is 1: return False
	if num % 2 is 0: return num is 2
	division = 3
	while (division * division) <= num:
		if num % division is 0:
			return False
		division += 2
	return True

def is_pandigit(num):
	'''
	Checks if a number is pandigital
	@param int
	@return boolean
	'''
	num, pandigit = str(num), ''
	length = len(num)
	'''generate a pandigit of length equal to num'''
	for x in range(1, length+1):
		pandigit += str(x)
	sorted_num = "".join(sorted(num))
	if sorted_num == pandigit: 
		return True
	else:
		return False

def main():
	(pandigit, prime_pandigit) = ([4321, 54321, 654321, 7654321, 87654321, 987654321], [])

	for x in pandigit:
		for num in itertools.permutations(str(x)):
			num = int("".join(num))
			if is_prime(num) and is_pandigit(num):
				prime_pandigit.append(num)

	return round(max(prime_pandigit) ** (1.0/5), 11)


if __name__ == "__main__":
	print(main())