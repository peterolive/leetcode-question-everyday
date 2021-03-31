from typing import List


class SolveNQueens:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        self.search(n, result, [])
        return result

    def search(self, n, result, track):
        if len(track) == n:
            result.append(self.draw(track))

        for current_col in range(n):
            if not self.is_valid(track, current_col):
                continue

            track.append(current_col)
            self.search(n, result, track)
            track.pop()

    def is_valid(self, track, current_col):
        for r, c in enumerate(track):
            if c == current_col:
                return False
            if abs(current_col - c) == abs(len(track) - r):
                return False
        return True

    def draw(self, track):
        board = []
        for i in range(len(track)):
            row = ['.'] * len(track)
            row[track[i]] = 'Q'
            row_str = ''.join(row)
            board.append(row_str)
        return board
