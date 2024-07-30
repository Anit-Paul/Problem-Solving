from typing import List

class Solution:
    # Function to detect cycle in an undirected graph.
    def __dfs(self, i, visit, parent, adj):
        visit[i] = True
        for j in adj[i]:
            if j == parent[i]:  
                continue
            if visit[j]:
                return 1
            parent[j] = i
            if self.__dfs(j, visit, parent, adj):
                return 1
        return 0
        
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visit = [False for _ in range(V)]
        parent = [-1 for _ in range(V)]  # Initialize parent with -1
        for i in range(V):
            if not visit[i]:
                if self.__dfs(i, visit, parent, adj):
                    return True
        return False
