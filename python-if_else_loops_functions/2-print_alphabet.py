#!/usr/bin/python3
def print_alphabet():
	"""Print the alphabet in lowercase."""
	for letter in range(ord('a'), ord('z') + 1):
		print(chr(letter), end='')
	print()  # for a new line after printing the alphabet
