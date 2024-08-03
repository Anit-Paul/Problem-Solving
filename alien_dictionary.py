from collections import defaultdict,deque
class Solution:
    def findOrder(self,a, N, K):
        map=defaultdict(list)
        #construction of the graph
        for i in range(1,len(a)):
            for j in range(0,min(len(a[i]),len(a[i-1]))):
                if(a[i-1][j]!=a[i][j]):
                    map[a[i-1][j]].append(a[i][j])
                    break
        in_deg=[0 for _ in range(k)]
        
        for key,value in map.items():
            for j in value:
                in_deg[ord(j)-ord('a')]+=1
        
        q=deque()
        for i in range(k):
            if in_deg[i]==0:
                q.append(chr(ord('a')+i))
                
        #toposort
        s=''
        while q:
            node=q.popleft()
            s+=node
            for j in map[node]:
                in_deg[ord(j)-ord('a')]-=1
                if(in_deg[ord(j)-ord('a')]==0):
                    q.append(j)
        return s
