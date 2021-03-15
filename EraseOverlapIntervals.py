from typing import List


class EraseOverlapIntervals:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        res = lo = 0

        for hi in range(1, len(intervals)):
            if intervals[lo][1] > intervals[hi][0]:
                res += 1
            if intervals[lo][1] < intervals[hi][0] or intervals[lo][1] > intervals[hi][1]:
                lo = hi

        return res
