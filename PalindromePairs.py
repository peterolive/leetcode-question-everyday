from typing import List


class PalindromePairs:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        self.map_ = {}

        for i, word in enumerate(words):
            self.map_[word] = i

        words = sorted(words, key=len)

        res = []

        for word in words:
            res.extend(self.get_palindrome(word))

        return res

    def get_palindrome(self, word, words):
        self.map_ = {}

        for i, word1 in enumerate(words):
            self.map_[word1] = i
        print(self.map_)
        ans = []

        for i in range(len(word) + 1):
            substring_p = word[:i][::-1]
            if substring_p == word:
                break
            if substring_p in self.map_ and self.is_palindrome(word + substring_p):
                ans.append([self.map_[word], self.map_[substring_p]])
        # print(ans)

        for i in range(len(word), 0, -1):
            substring_p = word[i:][::-1]
            print(substring_p)
            if substring_p == word:
                break
            if substring_p in self.map_ and self.is_palindrome(substring_p + word):
                ans.append([self.map_[substring_p], self.map_[word]])
        # print(ans)

        return ans

    def is_palindrome(self, word):
        if word == word[::-1]:
            return True

        return False
