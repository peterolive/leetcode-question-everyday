from typing import List


class Permute:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, path = [], []
        visited = [False] * len(nums)
        self.permutation(nums, result, path, visited)
        return result

    def permutation(self, nums, result, path, visited):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if visited[i]:
                continue
            path.append(nums[i])
            visited[i] = True
            self.permutation(nums, result, path, visited)
            visited[i] = False
            path.pop()
