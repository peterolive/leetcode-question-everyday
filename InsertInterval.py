from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return newInterval
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start > res[-1][1]:
                res.append(intervals[i])
            res[-1][1] = max(end, res[-1][1])

        return res
