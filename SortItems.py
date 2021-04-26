from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        out_degree_item = [[] for _ in range(n)]
        in_degree_item = [0] * n

        out_degree_group = [[] for _ in range(m)]
        in_degree_group = [0] * m

        for i in range(n):
            for item in beforeItems[i]:
                out_degree_item[item].append(i)
                in_degree_item[i] += 1
                if group[i] != group[item]:
                    out_degree_group[group[item]].append(group[i])
                    in_degree_group[group[i]] += 1

        item_order = self.bfs(out_degree_item, in_degree_item)
        group_order = self.bfs(out_degree_group, in_degree_group)
        if not item_order or not group_order:
            return []
        import collections
        order_within_group = collections.defaultdict(list)
        for v in item_order:
            order_within_group[group[v]].append(v)

        res = []
        for group in group_order:
            res += order_within_group[group]
        return res

    def bfs(self, out_degree, in_degree):
        queue = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        num_choose = 0
        res = []
        while queue:
            now_pos = queue.pop(0)
            num_choose += 1
            res.append(now_pos)
            for next_pos in out_degree[now_pos]:
                in_degree[next_pos] -= 1
                if in_degree[next_pos] == 0:
                    queue.append(next_pos)

        if num_choose == len(in_degree):
            return res
        return []
