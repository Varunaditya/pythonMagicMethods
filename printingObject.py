# A program that creates an object of the class and passes an argument with it.
# Genreally, passing the object to the print() function returns the memory address 
# of the object but by using dunder methods ot r magic methods, the passed string
# can be accessed.
# Author: Varunaditya Jadwal

class String:
	def __init__(self, string):
		self.string = string

	def __repr__(self):
		return self.string

if __name__ == '__main__':
	string1 = String('Hello, World')
	print(string1)