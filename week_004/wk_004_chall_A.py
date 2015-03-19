#!/usr/bin/python3
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
License type: MIT :)
Status: COMPLETED...
"""

def irrational_decimal(limit, index_limit, elements):
	product = j =1
	new_string = ''
	for i in range(1,limit+1):
		new_string += str(i)
		if len(new_string) >= index_limit:
			break

	for x in range(elements):
		product *= int(new_string[j-1])
		j *= 10

	return product

if __name__ == "__main__":
	print(irrational_decimal(10000000, 10**(6+1), 8))

