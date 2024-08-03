from collections import defaultdict,deque
class Solution(object):
    def canFinish(self, n, p):
        in_deg=[0 for _ in range(n)]
        map=defaultdict(list)
        for i in p:
            map[i[1]].append(i[0])
        for key,value in map.items():
            for j in value:
                in_deg[j]+=1
        q=deque()
        for i in range(0,n):
            if(in_deg[i]==0):
                q.append(i)
        while q:
            node=q.popleft()
            for j in map[node]:
                in_deg[j]-=1
                if(in_deg[j]==0):
                    q.append(j)
        for i in in_deg:
            if(i>0):
                return False
        return True        
