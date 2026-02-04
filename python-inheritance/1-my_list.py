#!/usr/bin/python3
"""
    This module defines a MyList class that inherits from list.
"""


class MyList(list):
	"""
	    MyList class that inherits from list
		and provides a method to print the list sorted.
	"""
	def print_sorted(self):
		"""
		    Prints the list in ascending order
			without modifying the original list.
		"""
		copy_list = self[:]
		copy_list.sort()
		print(str(copy_list))
