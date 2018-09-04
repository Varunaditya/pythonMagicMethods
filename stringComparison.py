class Word(str):
	def __new__(cls, word):
		if ' ' in word:
			print('The string contains spaces.\nTruncating the word till the first space.')
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
	string = Word('abc')
	print(string >= 'abe')
	print(string <= 'abe')
	print(string > 'abe')
	print(string < 'abe')
	print(string == 'abe')
	print(string != 'abe')