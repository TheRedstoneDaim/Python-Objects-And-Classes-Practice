
from Reverser import Reverser

wordToBeReversed = input("Enter a sentence which you want to reverse: ")
reverser = Reverser(wordToBeReversed)
print("The reversed sentence is:", reverser.reverse())
