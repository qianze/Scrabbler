#Qianze Zhang
#This is the front end (GUI) of the ScrabbleSolver desktop tool.
#Built on Tkinter

from tkinter import * #import all of tkinter module

from DicManager import DicManager

class Application(Frame):
	def __init__(self, rootWindow):
		super().__init__(rootWindow)
		self.grid()

		#variable for help option
		self.v = 0

		#All widgets below with grid

		#top widget giving intro to program
		self.intro = Message(self, width =120, text = "Welcome to Scrabble Solver!" +
			"\n\nChoose an option below for information and more directions.")
		self.intro.grid(row=1, column=1, rowspan=1, columnspan=1)

		#button widgets (left side)
		#anagrams
		self.but1 = Button(self, text="Anagrams", width=12)
		self.but1.grid(row=2, column=1, rowspan=1, columnspan=1, padx=5, pady=2.5)
		self.but1.bind("<Button-1>", self.info1)

		#highest score
		self.but2 = Button(self, text="Highest Score", width=12)
		self.but2.grid(row=3, column=1, rowspan=1, columnspan=1, padx=5, pady=2.5)
		self.but2.bind("<Button-1>", self.info2)

		#begins with
		self.but3 = Button(self, text="Begins With:", width=12)
		self.but3.grid(row=4, column=1, rowspan=1, columnspan=1, padx=5, pady=2.5)
		self.but3.bind("<Button-1>", self.info3)

		#ends with
		self.but4 = Button(self, text="Ends With:", width =12)
		self.but4.grid(row=5, column=1, rowspan=1, columnspan=1, padx=5, pady=2.5)
		self.but4.bind("<Button-1>", self.info4)

		#Q but not U
		self.but5 = Button(self, text="\"Q but not U\"", width=12)
		self.but5.grid(row=6, column=1, rowspan=1, columnspan=1, padx=5, pady=2.5)
		self.but5.bind("<Button-1>", self.info5)

		#X or Z with current tiles
		self.but6 = Button(self, text="X or Z", width=12)
		self.but6.grid(row=7, column=1, rowspan=1, columnspan=1,padx=5, pady=2.5)
		self.but6.bind("<Button-1>", self.info6)

		#word verifier
		self.but7 = Button(self, text="Word Verifier", width=12)
		self.but7.grid(row=8, column=1, rowspan=1, columnspan=1, padx=5, pady=2.5)
		self.but7.bind("<Button-1>", self.info7)

		#instructions widget
		self.infoSpace = Text(self, width = 44, height = 6)
		self.infoSpace.grid(row=1, column=2, rowspan=1, columnspan=2, padx=2.5, pady=2.5)
		self.infoSpace.config(state = "disabled")

		#entry widget for letter tiles
		self.txt2 = Text(self, width = 39, height = 1)
		self.txt2.grid(row=2, column=2, rowspan=1, columnspan=1, padx=2.5, pady=2.5)
		self.txt2.config(state = "normal")

		#go button
		self.goBut = Button(self, text="GO!", width = 4)
		self.goBut.grid(row=2, column =3, rowspan=1, columnspan =1, padx=1.5,pady=2.5)
		self.goBut.bind("<Button-1>", self.displayResults)

		#text widget for word display
		self.txt3 = Text(self, width =44, height=13)
		self.txt3.grid(row=3, column=2, rowspan=6, columnspan=2,padx=2.5,pady=2.5)
		self.txt3.config(state= "disabled")

	#input: string of letter tiles and int representing option chosen
	#output: True if tiles represent valid input, false if not
	'''
	def isValidInput(self, tiles, option)
		tiles = self.inputSpace.get(0.0, END)

		alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
		"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
		for tile in tiles:
			if tile not in alphabet and option != 5:
				#resets
				self.infoSpace.config(state = "normal")
				self.infoSpace.delete(0.0, END)
				self.infoSpace.insert(0.0, "Invalid tiles. Please reselect and try again.")
				self.infoSpace.config(state = "disabled")
				break
				'''
	'''
	each of the following functions display a different set of instructions
	that correspond to the options from the buttons
	'''
	def info1(self, event):#Anagrams
		info = "Gives a list of all words that can be made using every letter tile given.\n\n"
		info = info + "Please enter your tiles (lowercase, seperated by spaces) in the second textbox, then click GO!"

		self.infoSpace.config(state = "normal")
		self.infoSpace.delete(0.0, END)
		self.infoSpace.insert(0.0, info)
		self.infoSpace.config(state = "disabled")
		self.v = 1
		self.txt2.delete(0.0, END)

	def info2(self, event):#highest score
		info = "Gives a list of all words worth the highest possible score using all given tiles\n\n"
		info = info + "Please enter your tiles (lowercase, seperated by spaces) in the second textbox, then click GO!"

		self.infoSpace.config(state = "normal")
		self.infoSpace.delete(0.0, END)
		self.infoSpace.insert(0.0, info)
		self.infoSpace.config(state = "disabled")
		self.v = 2
		self.txt2.delete(0.0, END)

	def info3(self, event):#begins with
		info = "Gives a list of all words that begin with the given group of tiles (in the same sequence)\n\n"
		info = info + "Please enter your tiles (lowercase, no spaces) in the second textbox, then click GO!"

		self.infoSpace.config(state = "normal")
		self.infoSpace.delete(0.0, END)
		self.infoSpace.insert(0.0, info)
		self.infoSpace.config(state = "disabled")
		self.v = 3
		self.txt2.delete(0.0, END)

	def info4(self, event):#ends with
		info = "Gives a list of all words that end with the given group of tiles (in the same sequence)\n\n"
		info = info + "Please enter your tiles (lowercase, no spaces) in the second textbox, then click GO!"

		self.infoSpace.config(state = "normal")
		self.infoSpace.delete(0.0, END)
		self.infoSpace.insert(0.0, info)
		self.infoSpace.config(state = "disabled")
		self.v = 4
		self.txt2.delete(0.0, END)

	def info5(self, event):#qbutnotU
		info = "Gives a list of all words that start with a Q that is not followed with a U.\n\n"
		info = info + "Click GO!"

		self.infoSpace.config(state = "normal")
		self.infoSpace.delete(0.0, END)
		self.infoSpace.insert(0.0, info)
		self.infoSpace.config(state = "disabled")
		self.v = 5
		self.txt2.delete(0.0, END)

	def info6(self, event):#x or Z
		info = "Gives a list of all words that include a given tile and either X or Z.\n\n"
		info = info + "Please enter your tile in the second textbox, then click GO!"

		self.infoSpace.config(state = "normal")
		self.infoSpace.delete(0.0, END)
		self.infoSpace.insert(0.0, info)
		self.infoSpace.config(state = "disabled")
		self.v = 6
		self.txt2.delete(0.0, END)

	def info7(self, event):#wordVerifier
		info = "Verifies whether or not the given word is in the scrabble dictionary\n\n"
		info = info +"Please enter your word in the second textbox, then click GO!"

		self.infoSpace.config(state = "normal")
		self.infoSpace.delete(0.0, END)
		self.infoSpace.insert(0.0, info)
		self.infoSpace.config(state = "disabled")
		self.v = 7
		self.txt2.delete(0.0, END)

	def displayResults(self, event):
		option = self.v
		tiles = self.txt2.get(0.0, END)
		tiles = tiles[:-1]
		tiles.split(" ")
		print(tiles)

		alphabet = ['a', 'b', 'c', 'd', 'e', 'f', "g", "h", "i", "j", "k", 'l']
		alphabet.extend(["m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
		print(alphabet)
		for tile in tiles:
			print(tile)
			'''
			if tile not in alphabet:
				self.infoSpace.config(state = "normal")
				self.infoSpace.delete(0.0, END)
				self.infoSpace.insert(0.0, "Invalid tiles. Please reselect option on left and try again.")
				self.infoSpace.config(state = "disabled")
				'''

		wordFinder = DicManager("words.txt")

		if option == 1:
			words = wordFinder.anagrams(tiles)
		elif option == 2:
			words = wordFinder.highestScore(tiles)
		elif option == 3:
			words = wordFinder.beginsWith(tiles)
		elif option == 4:
			words = wordFinder.endsWith(tiles)
		elif option == 5:
			words = wordFinder.qbutNotU()
		elif option == 6:
			words = wordFinder.xOrZ(tiles)
		elif option == 7:
			answer = wordFinder.wordVerifier(tiles)

			#format output for user
		if option == 1 or option == 2 or option == 3 or option == 4 or option == 6 or option ==5 or option ==8:
			words = "\n".join(words)
		elif option == 7:
			if answer == True:
				words = "Word is valid."
			else:
				words = "Word is invalid."

				#display output to screen
		self.txt3.config(state = "normal")
		self.txt3.delete(0.0, END)
		self.txt3.insert(0.0, words)
		self.txt3.config(state = "disabled")

root = Tk()
root.title("Scrabble Solver")
root.geometry("500x365")
myApplication = Application(root)
root.mainloop()
