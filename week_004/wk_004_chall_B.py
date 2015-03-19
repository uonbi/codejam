#!/usr/bin/python3
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Truncatable primes eg 3797->379->37->3 and 3797->797->97->7)
License type: MIT :)
Status: COMPLETE...
"""
def is_prime(num):
	'''
	Check if a number is prime
	@param int
	@return boolean
	'''
	if num is 1:
		return False
	if num % 2 is 0:
		return num == 2
	division = 3
	while (division * division) <= num:
		if num % division == 0:
			return False
		division += 2

	return True

def is_truncatable(num):
	'''
	->is_truncatables a number digit by digit checking whether the new number is prime
	return the number if conditions are met otherwise 0
	@param int
	@return boolean
	'''
	flag = 1
	if is_prime(num):
		length = len(str(num))
		for i in range(1, length):
			r_to_l = int(str(num)[0:i])
			l_to_r = int(str(num)[length-i:])

			if is_prime(r_to_l) and is_prime(l_to_r):
				flag *= 2
			else:
				flag = 0

	return (0, num)[flag >= 2]

def main():
	tracker, i, limit, product =0, 23, 1000000, 1

	while i <= limit:
		if is_truncatable(i) != 0:
			product *= i
			tracker += 1
		i += 1
		if tracker == 11:
			return product
			
	return product


if __name__ == "__main__":
	print "Product of the 11 truncatable primes..."
	print main()