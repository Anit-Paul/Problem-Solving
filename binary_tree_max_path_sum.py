import sys
class Solution(object):
    def get_max(self,root,lst):
        if(root is None):
            return 0
        left=max(0,self.get_max(root.left,lst))
        right=max(0,self.get_max(root.right,lst))
        lst[0]=max(lst[0],right+left+root.val)
        return root.val+max(left,right)
    def maxPathSum(self, root):
        lst=[-sys.maxsize]
        if(root is None):
            return 0
        self.get_max(root,lst)
        return lst[0]
