from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            in_degree[node_in] += 1

        queue = []

        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        res = []
        num_choose = 0
        while queue:
            now_pos = queue.pop(0)
            num_choose += 1
            res.append(now_pos)
            for next_pos in graph[now_pos]:
                in_degree[next_pos] -= 1
                if in_degree[next_pos] == 0:
                    queue.append(next_pos)
        if num_choose == numCourses:
            return res
        return []
