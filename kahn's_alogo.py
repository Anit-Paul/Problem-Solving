from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, v, adj):
        in_deg={}
        for i in range(v):
            in_deg[i]=0
            
        for i in range(v):
            for j in adj[i]:
                in_deg[j]=in_deg.get(j)+1
        res=[]
        q=deque()
        for i in range(v):
            if(in_deg.get(i)==0):
                q.append(i)
        
        while q:
            node=q.popleft()
            res.append(node)
            for j in adj[node]:
                in_deg[j]-=1
                if in_deg.get(j)==0:
                    q.append(j)
            
        return res
            
