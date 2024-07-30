from typing import List
from collections import deque
class Solution:
    def bfs(Self,i,adj,visit,parent):
        q=deque()
        q.append(i)
        visit[i]=True
        while q :
            i=q.popleft()
            for j in adj[i]:
                if j==parent[i]:
                    continue
                elif(visit[j]):
                    return True
                else:
                    q.append(j)
                    visit[j]=True
                    parent[j]=i
        return False
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		visit=[False for _ in range(V)]
        parent=[-1 for _ in range(V)]
        for i in range(V):
            if not visit[i]:
                if self.bfs(i,adj,visit,parent):
                    return True
        return False
