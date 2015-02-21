#!/usr/bin/python3
"""
Author: Denis Karanja,
Lead, Sci CodeJam (codejam.sci.website)
email: dee.caranja@gmail.codejam

Task: Kitakale Kingdom Break In...(codejam.sci.website)
"""
import itertools, fractions, collections

def is_palindrome(string):
	"""Checks if a string is palindrome"""
	string = str(string)

	#return true if the string and it's reverse are the same
	return (string == string[::-1])

def valid_key(key):
	'''Checks if a key is valid for the main door'''
	key = str(key)
	pair_flag = 0
	if key == key[::-1]:
		return True
	else:
		#get frequency of characters
		col_dict = collections.Counter(key)

		for x, y in col_dict.items():
			#x is the key, and y is the frequency i.e the number of times the key occurs
			if y >= 2 and y < 4:#2 e.g yyjoo. <4 e.g aaacc
				pair_flag += 1

			elif y is 4:#eg zzzzm
				pair_flag += 2

			if pair_flag == 2:#matches the above logic
				return True

		return False

def is_a_valid_key(key):
	'''Checks is a key is valid for the main door. Uses permutations'''
	if is_palindrome(key):
		return True
	else:
		for anagram in set(itertools.permutations(key)):
			if is_palindrome("".join(anagram)):
				#if any anagram of 'key' has a palindrome, it is a valid key
				return True
		return False

def keys(key_bag):#permutations
	'''Returns the number of keys that can open the main door'''
	assert type(key_bag) is str
	key_count = 0
	key_holder = open(key_bag, "r")#read from the key_bag
	holder = []
	all_keys = ''

	#read all keys in key_bag
	for every_key in key_holder:
		all_keys += every_key

	#remove end of line charcter and make the string a list
	every_key = every_key.strip("\n").replace('"', "").replace(" ", "").split(",")

	#return the valid keys only i.e, those that give palindrome(s)
	for key in every_key:
		if is_a_valid_key(key):#this one uses itertools(permutations)-slower
			key_count += 1
			holder.append(key)

	#return the smallest fractions. This corresponds to the probability of picking
	#the right key to the main door
	probability = str(fractions.Fraction(key_count, len(every_key)))
	
	return (key_count, probability)

def find_keys(key_bag):#quick logic
	'''Returns the number of keys that can open the main door'''
	assert type(key_bag) is str
	key_count = 0
	key_holder = open(key_bag, "r")#read from the key_bag
	holder = []
	all_keys = ''

	#read all keys in key_bag
	for every_key in key_holder:
		all_keys += every_key

	#remove end of line charcter and make the string a list
	every_key = every_key.strip("\n").replace('"', "").split(",")

	#return the valid keys only i.e, those that give palindrome(s)
	for key in every_key:
		if valid_key(key):#this one uses some logic. Faster
			key_count += 1
			holder.append(key)

	#return the smallest fractions. This corresponds to the probability of picking
	#the right key to the main door
	probability = str(fractions.Fraction(key_count, len(every_key)))
	
	return (key_count, probability)
	

def read_file(file_name):
	with open(file_name, "r") as my_file:
		print(my_file.read())

if __name__ == "__main__":
	print(find_keys('key_bag.txt'))
	print(keys('key_bag.txt'))
	#read_file('key_bag.txt')
	