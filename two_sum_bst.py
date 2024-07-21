class Solution(object):
    def compute_result(self,root,k):
        lst=[]
        while root:
            if(root.left==None):
                if(lst and (k-root.val) in lst):
                    return True
                lst.append(root.val)
                root=root.right
            else:
                temp=root.left
                while(temp.right!=None and temp.right!=root):
                    temp=temp.right
                if(temp.right):
                    temp.right=None
                    if(lst and (k-root.val) in lst):
                        return True
                    lst.append(root.val)
                    root=root.right
                else:
                    temp.right=root
                    root=root.left
        return False
    def findTarget(self, root, k):
       return self.compute_result(root,k)
