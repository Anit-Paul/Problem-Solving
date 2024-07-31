from collections import deque
class Solution(object):
    def bfs(self,visit,color,graph,i):
        color[i]='g'
        visit[i]=1
        q=deque()
        q.append((i, 0))  
        while q:
            node, level = q.popleft()
            for neighbor in graph[node]:
                if visit[neighbor] == 0:
                    visit[neighbor] = 1
                    if level % 2 == 0:
                        color[neighbor] = 'b'
                    else:
                        color[neighbor] = 'g'
                    q.append((neighbor, level + 1))
                else:
                    if color[neighbor] == color[node]:
                        return False
        return True
    def isBipartite(self, graph):
        color=['w' for _ in range(len(graph))]
        visit=[0 for _ in range(len(graph))]
        for i in range(len(graph)):
            if(visit[i]==0):
                if(not self.bfs(visit,color,graph,i)):
                    return False
        return True


        
