

class Anagram: 
    def __init__(self, word="listen"):
        self.word = word

    def match(self, possible_anagrams):
        result = []
        sorted_word = sorted(self.word.lower()) 

        for word in possible_anagrams:
            sorted_word_candidate = sorted(word.lower())

            if sorted_word == sorted_word_candidate and self.word.lower() != word.lower():
                result.append(word)

        return result
    

        