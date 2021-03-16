from typing import List


class RemoveCoveredIntervals:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][1] > res[-1][1]:
                res.append(intervals[i])

        return len(res)
