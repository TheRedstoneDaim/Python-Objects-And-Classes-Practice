
class Reverser:
    wordToBeReversed = None
    def __init__(self, word):
        self.wordToBeReversed = word

    def reverse(self):
        wordToBeReversed = self.wordToBeReversed
        stringWords = wordToBeReversed.split()

        reversedStringWords = []
        a = len(stringWords) - 1
        for i in range(len(stringWords)):
            reversedStringWords.append(stringWords[a])
            a -= 1

        reversedString = " ".join(reversedStringWords)
        return reversedString
