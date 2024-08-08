class Disjoint_set:
    def __init__(self, n):
        self.__parent = [i for i in range(n)]
        self.__size = [1 for _ in range(n)]
        self.__rank = [0 for _ in range(n)]
    
    def find_parent(self, node):
        if node == self.__parent[node]:
            return node
        self.__parent[node] = self.find_parent(self.__parent[node])
        return self.__parent[node]  # Path compression 
    
    def union_by_rank(self, u, v):
        pu = self.find_parent(u)
        pv = self.find_parent(v)
        if self.__rank[pu] < self.__rank[pv]:
            self.__parent[pu] = pv
        elif self.__rank[pu] > self.__rank[pv]:
            self.__parent[pv] = pu
        else:
            self.__parent[pv] = pu
            self.__rank[pu] += 1
    
    def union_by_size(self, u, v):
        pu = self.find_parent(u)
        pv = self.find_parent(v)
        if(self.__size[pu]>self.__size[pv]):
            self.__parent[pv]=pu
            self.__size[pu]+=self.__size[pv]
        else:
            self.__parent[pu]=pv
            self.__size[pv]+=self.__size[pu]

def main():
    ds = Disjoint_set(7)
    ds.union_by_size(0, 1)
    ds.union_by_size(1, 2)
    ds.union_by_size(3, 4)
    ds.union_by_size(5, 6)
    ds.union_by_size(4, 5)
    if ds.find_parent(2) == ds.find_parent(6):
        print('same component')
    else:
        print('not in same component')
    ds.union_by_size(2, 6)
    if ds.find_parent(2) == ds.find_parent(6):
        print('same component')
    else:
        print('not in same component')
 
if __name__ == '__main__':
    main()
