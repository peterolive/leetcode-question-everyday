class TotalNQueens:
    def totalNQueens(self, n: int) -> int:
        result = []
        self.search(n, result, [])
        return len(result)

    def search(self, n, result, track_queen):
        if len(track_queen) == n:
            result.append(track_queen)

        for queen_col in range(n):
            if not self.is_valid(track_queen, queen_col):
                continue

            track_queen.append(queen_col)
            self.search(n, result, track_queen)
            track_queen.pop()

    def is_valid(self, track_queen, queen_col):
        for r, c in enumerate(track_queen):
            if queen_col == c:
                return False
            if abs(r - len(track_queen)) == abs(c - queen_col):
                return False
        return True
