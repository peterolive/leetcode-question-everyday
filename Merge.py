from typing import List


class Merge:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        import heapq
        heap = []
        for i in range(len(intervals)):
            heapq.heappush(heap, [intervals[i][0], intervals[i]])

        res = []
        res.append(heap[0][1])
        heapq.heappop(heap)

        for i in range(0, len(heap)):
            start, interval = heapq.heappop(heap)
            if start <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)

        return res
