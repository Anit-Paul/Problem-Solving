from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        dist = [float("inf") for _ in range(n)]
        q = deque()
        dist[src] = 0

        map = defaultdict(list)
        for i in flights:
            map[i[0]].append([i[1], i[2]])

        q.append([0, (src, 0)])
        #stop,(source,dist)
        while q:
            stop, (node, cost) = q.popleft()
            if stop > k:
                continue
            for neighbour, wt in map[node]:
                if wt + cost < dist[neighbour] and stop <= k:
                    dist[neighbour] = wt + cost
                    q.append((stop + 1, (neighbour, dist[neighbour])))

        if dist[dst] == float("inf"):
            return -1
        return dist[dst]
