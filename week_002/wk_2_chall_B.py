#!/usr/bin/python3
"""
Author: Denis Karanja,
Lead: Sci CodeJam
Email: dee.caranja@gmail.com
License type: MIT :)
Status: COMPLETE...
"""

def get_cubes(limit):
	"""Returns a list of cubes not exceeding the limit given"""
	cubes_list = []
	#start from 346 onwards
	for x in range(346, limit+1):
		cubes = pow(x, 3)
		cubes_list.append(cubes)
	return list(set((cubes_list)))


def permute(mycubes_list):
	"""Gets smallest cube with exactly '5' permutations that are cubes"""
	(counter, cubic_perms) = (0, []) #initialize

	for x in mycubes_list:
		#sort every cube
		sorted_x = sorted(str(x))
		for y in mycubes_list:
			#sort all the cubes in the list
			sorted_y = sorted(str(y))
			if sorted_x == sorted_y:#match found
				cubic_perms.append(y)
				counter += 1#increment counter by 1

			if counter == 5:#number of similar numbers is 5 i.e, has 5 permutations
				return min(cubic_perms)
		
		'''Reset counter and list'''
		counter = 0
		cubic_perms = []

def main():
	#get cubes of 1..10000
	cubes = get_cubes(10000)
	return permute(cubes)
	


if __name__ == "__main__":
	print(main())