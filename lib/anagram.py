# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Store the word in lowercase for case insensitivity

    def match(self, words):
        return [w for w in words if sorted(w.lower()) == sorted(self.word) and w.lower() != self.word]
