from typing import List
import string
numbers = list(range(10))
letters = string.ascii_lowercase + string.ascii_uppercase


class letterCasePermutation:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = []
        self.letter_case_permutation(result, S, "", 0)
        return result

    def letter_case_permutation(self, result, s, path, index):
        if len(path) == len(s):
            result.append(path)

        for i in range(index, len(s)):
            if s[i] in letters:
                self.letter_case_permutation(result, s, path + s[i], i + 1)
                self.letter_case_permutation(result, s, path + s[i].swapcase(), i + 1)
            else:
                self.letter_case_permutation(result, s, path + s[i], i + 1)

