#week 0 - challenges approach
================
CHALLENGE A (implemented in python (wk0_chall_A.py))

* Create a function that receives a nested array or list.
* If the list is empty, return None
* otherwise append the elements of the bigger list/array to another empty array/list iff the element is not a list/array.
* otherwise if the elements of the array/list are lists/array e.g [ [1], 3 ] do a recursive call
* Count the number of times a recursive call is made. This will correspond to the number of lists/arrays found nested
* Add one for the parent array/list
* Get the length of new array/list. This will correspond to the number of elements inside the parent array/list. Add (recursive_calls) made since a list/array inside another is said to be an element of that array.
* Return the number of elemnts and lists/arrays found.
