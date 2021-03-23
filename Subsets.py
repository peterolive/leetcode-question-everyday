from typing import List


class Subsets:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, path = [], []
        self.sub_sets(nums, result, path, 0)
        return result

    def sub_sets(self, nums, result, path, start):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.sub_sets(nums, result, path, i + 1)
            path.pop()

