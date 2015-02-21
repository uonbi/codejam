#!/usr/bin/python3
"""
A palindrome generator for strings
e.g -> 'deed', 'did', 'wow', 'nearaen'
"""
__author__ = "Denis Karanja"
__version__ = "1.0.0"

from itertools import product

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def is_palindrome(string):
	"""Checks if a string is palindrome"""
	string = str(string)

	#return true if the string and it's reverse are the same
	return (string == string[::-1])

def palindrome_generator(str_len):
	#filters return generators. Generators can only be used once
	x, z = filter(is_palindrome, ["".join(i) for i in product(chars, repeat=str_len)]), \
	filter(is_palindrome, ["".join(i) for i in product(chars, repeat=str_len)])

	count, pali_len = 0 , sum(1 for _ in z)#get the number of palindromes in the generator from the filter
	
	for y in x:
		#y = "".join(sorted(y[:len(y)-2].capitalize() + y[-2:].upper()))
		y = "".join(sorted(y))
		count += 1

		#write to file
		file_name = "angani_chall_B.txt"
		if count < pali_len:
			with open(file_name, "a") as challenge_file:
				challenge_file.write('"' + y + '", ')
		elif count == pali_len:
			with open(file_name, "a") as challenge_file:
				challenge_file.write('"' + y + '"')
				return "Palindromes written to '{}'".format(file_name), count

if __name__ == "__main__":
	print(palindrome_generator(5))
