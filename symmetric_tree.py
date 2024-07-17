class Solution(object):
    def __helper(self,left,right):
        if left is None and right is None :
            return True
        if left is None or right is None :
            return False
        return (left.val==right.val) and (self.__helper(left.left,right.right))and(self.__helper(left.right,right.left))
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.__helper(root.left,root.right)
