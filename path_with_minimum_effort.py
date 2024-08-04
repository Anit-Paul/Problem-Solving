import heapq


class helper:
    def __init__(self, i, j, d):
        self.i = i
        self.j = j
        self.d = d

    def __lt__(self, other):
        return self.d < other.d


class Solution:
    def is_safe(self, i, j, visit):
        if i < 0 or i >= len(visit):
            return False
        if j < 0 or j >= len(visit[0]):
            return False
        return True

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pq = []
        dist = [
            [float("inf") for _ in range(len(heights[0]))] for _ in range(len(heights))
        ]
        visit = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
        heapq.heappush(pq, helper(0, 0, 0))
        dist[0][0] = 0

        while pq:
            node = heapq.heappop(pq)
            i = node.i
            j = node.j
            d = node.d
            if i == len(heights) - 1 and j == len(heights[0]) - 1:
                return d
            if visit[i][j] == False:
                visit[i][j] = True
                # top
                if self.is_safe(i + 1, j, visit):
                    temp = max(d, abs(heights[i][j] - heights[i + 1][j]))
                    if dist[i + 1][j] > temp:
                        dist[i + 1][j] = temp
                        heapq.heappush(pq, helper(i + 1, j, temp))
                # bottom
                if self.is_safe(i - 1, j, visit):
                    temp = max(d, abs(heights[i][j] - heights[i - 1][j]))
                    if dist[i - 1][j] > temp:
                        dist[i - 1][j] = temp
                        heapq.heappush(pq, helper(i - 1, j, temp))
                # left
                if self.is_safe(i, j - 1, visit):
                    temp = max(d, abs(heights[i][j] - heights[i][j - 1]))
                    if dist[i][j - 1] > temp:
                        dist[i][j - 1] = temp
                        heapq.heappush(pq, helper(i, j - 1, temp))
                # right
                if self.is_safe(i, j + 1, visit):
                    temp = max(d, abs(heights[i][j] - heights[i][j + 1]))
                    if dist[i][j + 1] > temp:
                        dist[i][j + 1] = temp
                        heapq.heappush(pq, helper(i, j + 1, temp))

        return dist[-1][-1]
