from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_ = 0
        mask = 0
        for i in range(32, -1, -1):

            mask = mask | (1 << i)

            prefixes = set([mask & num for num in nums])

            best = max_ | (1 << i)

            for prefix in prefixes:
                match = best ^ prefix
                if match in prefixes:
                    max_ = best
                    break

        return max_
