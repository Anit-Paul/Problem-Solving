class edge :
    def __init__(self,i,j,w):
        self.i=i
        self.j=j
        self.w=w
    def __lt__(self,other):
        return self.w<other.w
        
class Disjoint_set:
    def __init__(self,n):
        self.__parent=[i for i in range(0,n)]
        self.__rank=[0 for _ in range(n)]
    def find_parent(self,u):
        if(u==self.__parent[u]):
            return u
        self.__parent[u]=self.find_parent(self.__parent[u])
        return self.__parent[u]
    def union_by_rank(self,u,v):
        pu=self.find_parent(u)
        pv=self.find_parent(v)
        if(pu==pv):
            return 0
        if(self.__rank[pu]<self.__rank[pv]):
            self.__parent[pu]=pv
        elif(self.__rank[pu]>self.__rank[pv]):
            self.__parent[pv]=pu
        else:
            self.__parent[pv]=pu
            self.__rank[pu]+=1
        return 1
            
class Solution:
    def spanningTree(self, v, adj):
        edges=[]
        for i in range(0,len(adj)):
            for j in adj[i]:
                edges.append(edge(i,j[0],j[1]))
        cost=0
        edges.sort()
        d=Disjoint_set(v)
        for e in edges:
            if(d.union_by_rank(e.i,e.j)==1):
                cost+=e.w
        return cost
    
