from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        import heapq
        heap = []

        if not intervals:
            return 0

        intervals = sorted(intervals, key= lambda x: x.start)

        heapq.heappush(heap, intervals[0].end)

        for i in range(1, len(intervals)):
            meeting_end = heapq.heappop(heap)
            if meeting_end > intervals[i].start:
                heapq.heappush(heap, meeting_end)
            heapq.heappush(heap, intervals[i].end)

        return len(heap)
