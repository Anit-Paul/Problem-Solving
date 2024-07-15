#diameter is longest path between one node to another node
# it may or may not include root node
class Solution(object):
    def get_diameter(self,root,lst):
        if(root is None):
            return 0
        left=self.get_diameter(root.left,lst)
        right=self.get_diameter(root.right,lst)
        lst[0]=max(lst[0],left+right)
        return 1+max(left,right)
    def diameterOfBinaryTree(self, root):
        lst=[0]
        self.get_diameter(root,lst)
        return lst[0]
        
