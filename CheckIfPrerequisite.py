from typing import List


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]

        for node_in, node_out in prerequisites:
            graph[node_in].append(node_out)

        res = []

        def bfs(node1, node2):
            queue = []
            queue.append(node1)
            visited = set()
            while queue:
                now_pos = queue.pop(0)
                if now_pos == node2:
                    return True
                for next_pos in graph[now_pos]:
                    if next_pos not in visited:
                        queue.append(next_pos)
                        visited.add(next_pos)

            return False

        for node_in, node_out in queries:
            res.append(bfs(node_in, node_out))

        return res
