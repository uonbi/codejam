#!/usr/bin/python3
"""
Author: Denis Karanja,
Lead, Sci Code Jam (codejam.sci.website)
Task: Fibonacci word sum
Status:...COMPLETED
"""
def fibonacci(num):
	'''Return the fibonacci of a number'''
	x, y, z = 0, 1, 1
	for w in range(num+1):
		x = y
		y = z
		z = x + y
	return x

def main():
	#dictionary to hold alphabet's equivalents
	alphabet_equivalent = dict(a = 1,b = 2,c = 3,d = 4,e = 5,f = 6,g = 7,h = 8,i = 9,j = 10,k = 11,l = 12,m = 13,
		n = 14,o = 15,p = 16,q = 17,r = 18,s = 19,t = 20,u = 21,v = 22,w = 23,x = 24,y = 25,z = 26)

	#read from file
	file_handle = open("hexa.txt", "r")

	#initialize output counter
	word_sum = 0
	
	for x in file_handle:
		#remove the end of line and any spaces
		x = x.replace("\n", "").replace(" ", "")
		for single in x:
			if alphabet_equivalent.__contains__(single):
				#if string is a character, get equivalent and find it's fibonacci
				equi = alphabet_equivalent.get(single)
				word_sum += fibonacci(equi)
			else:
				#if string is a number, just get it's fibonacci
				word_sum += fibonacci(int(single))

	return word_sum

if __name__ == "__main__":
	print(main())