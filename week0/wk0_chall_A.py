#!/usr/bin/python3
"""
Author: Denis Karanja,
Lead, Sci Code Jam (codejam.sci.website)
Task: Flat array
Status:...COMPLETED

"""

calls = 1
flat_list = []

def flatten_list(my_list):
  '''Flattens a nested array and returns (A, E) where A is the number of elements
  present and E is the number of arrays/lists found'''
  global calls
  if type(my_list) is not list:
    raise TypeError("flatten_list() expects a list. {} given ".format(type(my_list)))
  elif type(my_list) is list:
    #check if list is null
    if len(my_list) is not 0:
      for i, inner_elem in enumerate(my_list):
        #check if elements inside list is a list
        if type(inner_elem) is list and len(inner_elem) is not 0:
          calls += 1
          flatten_list(inner_elem)
        else:
          flat_list.append(inner_elem)
    else: return "Empty list."
  return ( (len(flat_list) + (calls - 1)), calls)

print(flatten_list(["Denis", ["Array"], ["3"], 4, 7, 8]))