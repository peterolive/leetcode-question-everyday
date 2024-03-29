"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        if not intervals:
            return True
        import heapq
        intervals = sorted(intervals, key=lambda x: x.start)
        heap = []
        heapq.heappush(heap, intervals[0].end)
        meeting_end = intervals[0].end
        
        for i in range(1, len(intervals)):
            if intervals[i].start < meeting_end:
                return False
            else:
                meeting_end = intervals[i].end
                
        return True