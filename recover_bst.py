class Solution(object):
    def __init__(self):
        self.first=None
        self.middle=None
        self.last=None
        self.prev=TreeNode(float('-inf'))
    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        if(self.prev.val>root.val):
            if(self.first is None):
                self.first=self.prev
                self.middle=root
            else:
                self.last=root
        self.prev=root
        self.inorder(root.right)
    def recoverTree(self, root):
        self.inorder(root)
        if(self.first and self.last):
            temp=self.first.val
            self.first.val=self.last.val
            self.last.val=temp
        elif(self.first and self.middle):
            temp=self.first.val
            self.first.val=self.middle.val
            self.middle.val=temp
