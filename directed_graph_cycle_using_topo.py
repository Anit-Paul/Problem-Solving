from typing import List
from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, v : int , adj : List[List[int]]) -> bool :
        # code here
        in_deg=[0 for _ in range(v)]
        
        for i in range(v):
            for j in adj[i]:
                in_deg[j]+=1
        q=deque()       
        for i in range(v):
            if(in_deg[i]==0):
                q.append(i)
                
        while q:
            node=q.popleft()
            for j in adj[node]:
                in_deg[j]-=1
                if(in_deg[j]==0):
                    q.append(j)
        for i in in_deg:
            if i>0:
                return True
        
        return False
