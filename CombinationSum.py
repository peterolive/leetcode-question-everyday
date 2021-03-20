from typing import List


class CombinationSum:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        result, path = [], []
        self.combination_sum(candidates, 0, result, path, target)
        return result

    def combination_sum(self, nums, start, result, path, target):
        if target == 0:
            result.append(path[:])
            return

        for i in range(start, len(nums)):
            if nums[i] > target:
                return
            path.append(nums[i])
            self.combination_sum(nums, i, result, path, target - nums[i])
            path.pop()
