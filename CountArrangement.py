class CountArrangement:
    def countArrangement(self, n: int) -> int:
        result, path = [], []
        self.count_arrangement(result, path, set(), n)
        return len(result)

    def count_arrangement(self, result, path, visited, n):
        if len(path) == n:
            result.append(path[:])

        for i in range(1, n + 1):
            if i in visited:
                continue

            if i % (len(path) + 1) != 0 and (len(path) + 1) % i != 0:
                continue

            path.append(i)
            visited.add(i)
            self.count_arrangement(result, path, visited, n)
            visited.remove(i)
            path.pop()

    def is_valid(self, path):
        for i, p in enumerate(path):
            if p % (i + 1) != 0 and (i + 1) % p != 0:
                return False
        return True
