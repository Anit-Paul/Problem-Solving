class Solution:
    def traverse(self,root,lst,res):
        lst.append(root.data)
        if(root.left is None and root.right is None):
            res.append(list(lst))
            lst.pop()
            return
        if root.left is not None:
            self.traverse(root.left,lst,res)
        if root.right is not None:
            self.traverse(root.right,lst,res)
        lst.pop()
                
                
        
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        # code here
        res=[]
        lst=[]
        self.traverse(root,lst,res)
        return res
