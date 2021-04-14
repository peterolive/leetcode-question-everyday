from typing import List


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        import math
        def dfs(numbers):
            if len(nums) <= 2:
                return 1
            left = [num for num in numbers if num < numbers[0]]
            right = [num for num in numbers if num > numbers[0]]
            return math.comb(len(left) + len(right), len(right) * dfs(left) * dfs(right))

        return (dfs(nums) - 1) % (10**9 + 7)
