from typing import List


class CombinationSum3:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result, path = [], []
        self.combination_sum3(result, path, 1, n, k)
        return result

    def combination_sum3(self, result, path, start, target, k):
        if target == 0 and k == 0:
            result.append(path[:])

        for i in range(start, 10):
            if i > target:
                return
            if k < 0:
                return
            path.append(i)
            k -= 1
            self.combination_sum3(result, path, i + 1, target - i, k)
            k += 1
            path.pop()
