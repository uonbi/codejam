#!/usr/bin/python3
"""
Author: Denis Karanja,
Lead: Sci CodeJam
Email: dee.caranja@gmail.com,
TASK: It can be seen that the number, 125874, and its double, 251748, contain exactly 
			the same digits,
 			but in a different order.
			Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
def is_permuted(x, y):
	"""Checks if two numbers are permutations of each other"""
	x = "".join(sorted(str(x)))
	y = "".join(sorted(str(y)))
	return(False, True)[x == y] #if x is equal to y, return true, otherwise false

def main():
	x = 10
	while True:
		a, b, c, d, e = 2*x, 3*x, 4*x, 5*x, 6*x
		#check that the first two are permutations of each other
		if is_permuted(x, a) and is_permuted(x, b):
			#check the other three
			if is_permuted(x, c) and is_permuted(x, d) and is_permuted(x, e):
				return x
		x += 1

if __name__ == "__main__":
	print(main())