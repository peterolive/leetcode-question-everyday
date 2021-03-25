from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result, path = [], []
        visited = [False] * len(nums)
        self.permute_unique(nums, result, path, visited)
        return result

    def permute_unique(self, nums, result, path, visited):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                continue

            path.append(nums[i])
            visited[i] = True
            self.permute_unique(nums, result, path, visited)
            visited[i] = False
            path.pop()
