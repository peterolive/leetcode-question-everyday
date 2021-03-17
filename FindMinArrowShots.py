from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points = sorted(points, key=lambda x: (x[0], -x[1]))

        res = 0
        start, end = points[0]
        res += 1
        for i in range(1, len(points)):
            new_start, new_end = points[i]
            if end > new_end:
                end = new_end
            elif end < new_start:
                res += 1
                end = new_end
        return res
