from typing import List


class IntervalIntersection:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList and not secondList:
            return []
        import heapq

        heap = []

        i = 0
        while i < len(firstList) or i < len(secondList):
            if i < len(firstList):
                heapq.heappush(heap, [firstList[i][0], firstList[i]])
            if i < len(secondList):
                heapq.heappush(heap, [secondList[i][0], secondList[i]])
            i += 1

        res = []
        first = heapq.heappop(heap)
        end = first[1][1]

        while heap:
            start_at, interval = heapq.heappop(heap)
            if interval[0] <= end:
                res.append([interval[0], min(end, interval[1])])
            end = max(end, interval[1])

        return res
