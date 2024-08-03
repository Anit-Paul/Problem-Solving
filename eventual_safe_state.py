from collections import defaultdict,deque
class Solution(object):
    def eventualSafeNodes(self, graph):
        map=defaultdict(list)
        for i in range(len(graph)):
            for j in graph[i]:
                map[j].append(i)
        q=deque()
        for i in range (len(graph)):
            if(len(graph[i])==0):
                q.append(i)
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for j in map[node]:
                graph[j].remove(node)
                if(len(graph[j])==0):
                    q.append(j)
        res.sort()
        return res
