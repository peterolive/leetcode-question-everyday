from typing import List


class Combine:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, path = [], []
        self.com_bine(result, path, n, k, 0)
        return result

    def com_bine(self, result, path, n, k, start):
        if len(path) == k:
            result.append(path[:])

        for i in range(start, n):
            path.append(i + 1)
            self.com_bine(result, path, n, k, i + 1)
            path.pop()
