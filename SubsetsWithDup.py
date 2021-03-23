from typing import List


class SubsetsWithDup:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, path = [], []
        self.subsets_withdups(nums, result, path, 0)
        return result

    def subsets_withdups(self, nums, result, path, start):
        result.append(path[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])
            self.subsets_withdups(nums, result, path, i + 1)
            path.pop()
