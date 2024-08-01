def dfs(self,i,adj,visit,rs):
        
        visit[i]=True
        rs[i]=1
        for j in adj[i]:
            if(not visit[j]):
                if(self.dfs(j,adj,visit,rs)==True):
                    return True
            elif rs[j]==1:
                return True
            
        rs[i]=0
        return False
    
    def isCyclic(self, v : int , adj : List[List[int]]) -> bool :
        # code here
        
        visit=[False for _ in range (v)]
        rs=[0 for _ in range(v)]
        
        for i in range(0,v):
            if(not visit[i]):
                if(self.dfs(i,adj,visit,rs)==True):
                    return True
        
        return False
