#Qianze Zhang

class DicManager(object):
	def __init__(self, words):
		#read words.txt into a list
		self.__words = words
		self.__wordsList = []
		fileIn = open(words, "r")
		for line in fileIn:
			self.__wordsList.append(line[:-1])

	#Input: A string of letter tiles
	#Output: a list of all words that can be made using every letter tile given
	def anagrams(self, tiles):
		words = []
		letters = tiles.split()
		#make a dictionary of the letters
		letterCount = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0,
		'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0,
		't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
		#add values to dictionary
		for letter in letters:
			letterCount[letter] = letterCount[letter] + 1
		#for each word, create a letterCount dictionary and compare to original letterCount
		for word in self.__wordsList:
			if (len(word) == len(letters)):
				curLetterCount = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0,
		'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0,
		't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
			#if all key values in curLetterCount are <= those in words
				for letter in word:
					curLetterCount[letter] =curLetterCount[letter] +1
					matches = 0
				for key in curLetterCount:
					if(curLetterCount[key]<=letterCount[key]):
						matches = matches+1
					if(matches==26):
						words.append(word) #append word to words
		return words

	#Input: none
	#Output: a list of all words that start with a q that is not followed with a u
	def qbutNotU(self):
		words = []
		for item in self.__wordsList:
			if item[:1] == "q" and item[1:2] != "u":
				words.append(item)
		return words

	#Input: a word as a string
	#Output: a boolean: True if word is included in scrabble dictionary, False if not
	def wordVerifier(self, word):
		if word in self.__wordsList:
			return True
		else:
			return False

	#Input: a group of tiles as a string, representing the prefix of the word
	#Output: a list of all words that begin with that group of tiles (in the same sequence)
	def beginsWith(self, prefix):
		words = []
		for item in self.__wordsList:
			if(prefix == item[:len(prefix)]):
				words.append(item)
		return words

	#Input: a group of tiles as a string
	#Output: a list of all words that end with that group of tiles (in the same sequence)
	def endsWith(self, suffix):
		words = []
		for item in self.__wordsList:
			if suffix == item[-len(suffix):]:
				words.append(item)
		return words

	#Input: a single-character string representing a letter tile
	#Output: a list of all words containing that letter and X or Z
	def xOrZ(self, tile):
		words = []
		for item in self.__wordsList:
			if tile in item and "x" in item:
				words.append(item)
			elif tile in item and "z" in item:
				words.append(item)
		return words

	#Input: a string representing scrabble letter tiles
	#Output: list of the words worth the highest possible score using all given tiles
	def highestScore(self, tiles):
		words = self.anagrams(tiles)
		letterValues = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4,
		'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1,
		't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}
		maxValue = 0
		wordValues ={} #dictionary containing all word values
		maxWords = [] #list of all words worth maxValue
		for word in words:
			val = 0
			for letter in word:
				val = val + letterValues[letter]
			if(val > maxValue):
				maxValue = val
			wordValues[word] = val
		for key in wordValues:
			if(wordValues[key]==maxValue):
				maxWords.append(key)
		return maxWords

	#test method to view full wordsList
	def getWordsList(self):
		return self.__wordsList

def main():
	#prints entireWorldslist
	dictionary = DicManager("words.txt")

	'''
	print(dictionary.getWordsList())
	'''
	'''
	#test anagrams (works)
	anagrms = dictionary.anagrams("a p p e l")
	print(anagrms)
	'''

	#test q but not u
	'''
	qU = dictionary.qbutNotU()
	print(qU)
	'''

	#testing word verifier
	'''
	print(dictionary.wordVerifier("asdfdsf"))
	print(dictionary.wordVerifier("apple"))
	print(dictionary.wordVerifier("zoo"))
	'''

	#testing prefix function
	'''
	print(dictionary.beginsWith("green"))
	'''

	#testing suffix function
	'''
	print(dictionary.endsWith("ary"))
	'''

	#testing xOrZ
	'''
	print(dictionary.xOrZ("q"))
	'''

	#testing highestScore
	'''
	print(dictionary.highestScore("e a t s"))
	'''


main()
