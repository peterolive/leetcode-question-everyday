from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, path = [], []
        self.par_tition(result, path, 0, s)
        return result

    def par_tition(self, result, path, start_index, s):
        if start_index == len(s):
            result.append(path[:])

        for i in range(start_index, len(s)):
            if self.is_palindrome(s[start_index:i + 1]):
                path.append(s[start_index:i + 1])
                self.par_tition(result, path, i + 1, s)
                path.pop()

    def is_palindrome(self, substr):
        if substr == substr[::-1]:
            return True
        return False
