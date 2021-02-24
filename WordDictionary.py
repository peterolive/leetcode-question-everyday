class WordDictionary:

    def __init__(self):
        from collections import defaultdict
        """
        Initialize your data structure here.
        """
        self.words = defaultdict(list)

    def addWord(self, word: str) -> None:
        self.words[len(word)].append(word)

    def search(self, word: str) -> bool:
        if not self.words.get(len(word)):
            return False
        for w in self.words.get(len(word)):
            i = 0
            while i < len(word):
                if w[i] == word[i] or word[i] == '.':
                    i += 1
                else:
                    break
            if i == len(word):
                return True

        return False
