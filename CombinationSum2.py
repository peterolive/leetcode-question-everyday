from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        result, path = [], []
        self.combination_sum2(candidates, 0, path, result, target)
        return result

    def combination_sum2(self, nums, start, path, result, target):
        if not target:
            result.append(path)
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            if nums[i] > target:
                return
            path.append(nums[i])
            self.combination_sum2(nums, i + 1, path + [nums[i]], result, target-nums[i])
            path.pop()
