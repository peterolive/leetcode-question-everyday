class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        graph = self.build_graph(words)
        if not graph:
            return ''
        return self.topological_sort(graph)

    def build_graph(self, words):
        import collections
        graph = {}
        for word in words:
            for c in word:
                graph[c] = set()

        n = len(words)

        for i in range(n-1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i+1][j]:
                    graph[words[i][j]].add(words[i+1][j])
                    break
                if j == min(len(words[i]), len(words[i + 1])) - 1:
                    if len(words[i]) > len(words[i + 1]):
                        return None
        return graph

    def topological_sort(self, graph):
        in_degree = {node: 0 for node in graph}

        for node in graph:
            for neighbor in graph[node]:
                in_degree[neighbor] += 1

        queue = [node for node in in_degree if in_degree[node] == 0]

        import heapq
        heapq.heapify(queue)

        topo_order = ''
        while queue:
            now_pos = heapq.heappop(queue)
            topo_order += now_pos
            for next_pos in graph[now_pos]:
                in_degree[next_pos] -= 1
                if in_degree[next_pos] == 0:
                    heapq.heappush(queue, next_pos)

        if len(topo_order) == len(graph):
            return topo_order

        return ''
