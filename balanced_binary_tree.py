class Solution(object):
    def get_height(self,root):
        if(root is None):
            return [0,True]
        left_height,left_balance=self.get_height(root.left)
        right_height,right_balance=self.get_height(root.right)
        current_height=max(left_height,right_height)+1
        current_balance=(left_balance and right_balance) and (abs(right_height-left_height)<=1)
        return [current_height,current_balance]
        
    def isBalanced(self, root):
        if(root is None):
            return True
        h,b=self.get_height(root)
        return b
