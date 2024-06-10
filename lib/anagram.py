
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        anagrams = []
        sorted_word = sorted(self.word)

        for candidate in candidates:
            candidate_lower = candidate.lower()
            if candidate_lower != self.word and sorted(candidate_lower) == sorted_word:
                anagrams.append(candidate)

        return anagrams
