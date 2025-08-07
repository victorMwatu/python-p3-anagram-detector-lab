class Anagram():
    def __init__(self, word):
        self.word = word

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, word):
        if type(word) == str and 1 <= len(word) <= 25:
            self._word = word
        else:
            raise ValueError("Word must be between 1 and 25 alphabetic characters")

    def match(self, wordList):
        matches = []
        compare = self._word.lower()
        for w in wordList:
            if sorted(w.lower()) == sorted(compare):
                matches.append(w)
        # print(matches)
        return matches



