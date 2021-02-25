from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        from collections import defaultdict
        self.table = defaultdict(dict)
        for index, word in enumerate(words):
            for i in range(0, len(word) + 1):
                for j in range(len(word)):
                    self.table[word[:i]][word[j:]] = index

    def f(self, prefix: str, suffix: str) -> int:
        if suffix not in self.table[prefix]:
            return -1

        return self.table[prefix][suffix]

