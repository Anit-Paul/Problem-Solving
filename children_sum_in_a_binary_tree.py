class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes
    def helper(self,root):
        if root.left is None and root.right is None:
            return (root.data,1)
        left,lst=(0,1)
        right,rst=(0,1)
        if root.left is not None:
            left,lst=self.helper(root.left)
        if root.right is not None:
            right,rst=self.helper(root.right)
        st=0
        if(left+right==root.data):
            st=1
        return (left+right,st and lst and rst)
            
        
        
        
    def isSumProperty(self, root):
        # code here
        if(root is None):
            return 1
        sum,st=self.helper(root)
        return st
