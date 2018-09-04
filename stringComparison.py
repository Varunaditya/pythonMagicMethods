# A program that overloads the <, >, <= and >= operators for strings using the following dunder methods
# __new__ -> since string is immutable, it needs to be initialized
# __gt__ -> greater than | >
# __lt__ -> less than | <
# __ge__ -> greater or equal  | >=
# __gt__ -> less or equal | <=
# The program doesn't overloads the == and != opertaors as that will break the basic funcnality needed 
# while comparing the strings. Since, we didn't overload those operators, their funcnality remains intact.

class Word(str):
	def __new__(cls, word):
		#removing spaces from the strings
		if ' ' in word:
			print('The string contains spaces.\nTrimming the word till the first space.')
			word = word[:word.index(' ')]
		return str.__new__(cls, word)

	def __gt__(self, other):
		return len(self) > len(other)

	def __lt__(self, other):
		return len(self) < len(other)

	def __ge__(self, other):
		return len(self) >= len(other)

	def __le__(self, other):
		return len(self) <= len(other)

if __name__ == '__main__':
	string1 = Word('abc')
	string2 = Word('abe')
	print(string1 >= string2)
	print(string1 <= string2)
	print(string1 > string2)
	print(string1 < string2)
	print(string1 == string2)
	print(string1 != string2)
