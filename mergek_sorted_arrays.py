# 486 · Merge K Sorted Arrays
# https://www.lintcode.com/problem/486/
from typing import (
    List,
)

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergek_sorted_arrays(self, arrays: List[List[int]]) -> List[int]:
        # write your code here
        import heapq
        heap = []

        for i in range(len(arrays)):
            if arrays[i]:
                heapq.heappush(heap, (arrays[i][0], 0, i))

        if not heap:
            return heap

        res = []
        while heap:
            value, index, array_index = heapq.heappop(heap)
            # print(value, index, array_index)
            res.append(value)
            if index + 1 < len(arrays[array_index]):
                heapq.heappush(heap, (arrays[array_index][index + 1], index+ 1, array_index))

        return res
