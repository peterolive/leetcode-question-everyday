from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            in_degree[node_in] += 1

        num_choose = 0
        queue = []

        for key in in_degree:
            if in_degree[key] == 0:
                queue.append(key)

        print(in_degree)

        while queue:
            now_pos = queue.pop(0)
            num_choose += 1
            for next_pos in graph[now_pos]:
                in_degree[next_pos] -= 1
                if in_degree[next_pos] == 0:
                    queue.append(next_pos)

        return num_choose == numCourses
