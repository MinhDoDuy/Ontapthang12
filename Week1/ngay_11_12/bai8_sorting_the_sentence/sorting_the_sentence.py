class Solution:
    def sortSentence(self, s):
        parts = s.split()

        def get_index(word):
            return int(word[-1])

        parts.sort(key=get_index)

        new_sentence = []
        for w in parts:
            new_sentence.append(w[:-1])
        return " ".join(new_sentence)
