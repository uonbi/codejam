#!/usr/bin/python3
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Lead, SCI CodeJam
Email: dee.caranja@gmail.com,
Task: (Circular primes)
License type: MIT :)
Status: COMPLETED...
"""

def can_rotate_to_prime(num):
	'''
	-> can_rotate_to_primes a number from left to right
	@param int
	@return boolean
	'''
	flag, num, length = (1, str(num), len(str(num)))

	for x in range(0, length):
		if x < length:
			new_num = int(num[x+1:] + num[0:x+1])
			if is_prime(new_num):
				continue
			else:
				return False

	return True

def is_prime(num):
	'''
	-> Checks if a number is prime
	@param num int
	@return boolean
	'''
	if num is 1:
		return False
	if num % 2 is 0:
		return num is 2

	division = 3
	while (division * division) <= num:
		if num % division is 0:
			return False
		division += 2
	return True


def fibonacci(num):
	'''
	-> Populate the Fibonacci series
	@param num int
	@return int/long 
	'''
	a, b, c = 0, 1, 1
	for x in range(1, num+1):
		a = b
		b = c
		c = a + b
	return a


def main(limit):
	circular_sum = 13#start from 100
	print("Calculating circular primes below {}".format(limit))
	for x in range(100, limit):
		if can_rotate_to_prime(x):
			circular_sum += 1

	return fibonacci(circular_sum)

if __name__ == "__main__":
	print(main(10**6))
