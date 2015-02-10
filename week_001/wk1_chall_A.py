#!/usr/bin/python3
"""
Author: Denis Karanja,
Lead, Sci Code Jam (codejam.sci.website)
Task: Divisibility sum(simple)
Status:...COMPLETED
"""

#condensed form. sum() is efficient since it is inbuilt
def divisible(limit, prime_1 = 7, prime_2 = 11):
	return sum([x for x in range(1, limit) if (x % prime_1 is 0) and (x % prime_2 is 0) ])

#open form 
def main(limit, sum_of_x = 0):
	for x in range(1, limit):
		if x % 7 is 0 and x % 11 is 0:
			sum_of_x += x

	return sum_of_x

if __name__ == "__main__":
	print(divisible(10000))