from typing import List
map_ = {'2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result, path = [], []
        self.letter_combinations(digits, result, path, 0)
        return result

    def letter_combinations(self, digits, result, path, index):
        if index == len(digits):
            result.append(''.join(path[:]))
            return

        for letter in map_[digits[index]]:
            path.append(letter)
            self.letter_combinations(digits, result, path, index + 1)
            path.pop()
