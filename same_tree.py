from collections import deque
class Solution(object):
    def bfs_traversal(self,root,lst):
        q=deque()
        q.append(root)
        
        while q:
            temp = q.popleft()
            if temp:
                lst.append(temp.val)
                q.append(temp.left)
                q.append(temp.right)
            else:
                lst.append(None)
            
            
    def isSameTree(self, p, q):
        lst1=[]
        lst2=[]
        self.bfs_traversal(p,lst1)
        self.bfs_traversal(q,lst2)
        print(lst1,lst2)
        return lst1==lst2
