#!/usr/bin/python3
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics,
Email: dee.caranja@gmail.com,
Task: (Amicable numbers product)
Status.. COMPLETED...
"""
import math

def get_divisors_sum(num):
	'''
	-> get divisors sum of a number
	@param int
	@return int
	'''
	div_sum = 1
	for x in range(2, int(math.sqrt(num)) +1):
		if num % x == 0:
			div_sum += x
			div_sum += num//x
	return div_sum

def main(limit, amicable = []):
	print("Calculating amicable numbers product below {}...".format(limit))
	amicable_prod = 1
	for i in range(1, limit):
		if i == get_divisors_sum(get_divisors_sum(i)) and (i != get_divisors_sum(i)):
			amicable.extend ([i, get_divisors_sum(i)] )
			
	for x in set(amicable):
		amicable_prod *= x

	return (amicable_prod)

if __name__ == "__main__":
	print(main(10000))

