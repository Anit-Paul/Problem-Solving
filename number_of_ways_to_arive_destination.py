import heapq
from collections import defaultdict


class pair:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = (10**9) + 7
        dist = [float("inf") for _ in range(n)]
        way = [0 for _ in range(n)]

        # graph construction
        graph = defaultdict(list)
        for i in roads:
            graph[i[0]].append([i[1], i[2]])
            graph[i[1]].append([i[0], i[2]])
        # dijkstra
        q = []
        dist[0] = 0
        way[0] = 1
        heapq.heappush(q, pair(0, 0))
        while q:
            p = heapq.heappop(q)
            node = p.node
            cost = p.cost
            if node != n - 1:
                for j, wt in graph[node]:
                    if dist[j] > cost + wt:
                        dist[j] = cost + wt
                        way[j] = way[node] % mod
                        heapq.heappush(q, pair(j, dist[j]))
                    elif dist[j] == cost + wt:
                        way[j] = (way[j] + way[node]) % mod
        return way[n - 1]
