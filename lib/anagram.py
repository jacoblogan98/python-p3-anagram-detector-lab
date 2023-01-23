class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, poss_matches):
        matches = []
        for word in poss_matches:
            if(sorted([letter for letter in word]) == sorted([letter for letter in self.word])):
                matches.append(word)

        return matches