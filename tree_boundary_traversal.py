class Solution:
    def left_boundary(self, root, lst):
        temp = root.left
        while temp:
            if temp.left is not None or temp.right is not None:
                lst.append(temp.data)
            if temp.left is not None:
                temp = temp.left
            elif temp.right is not None:
                temp = temp.right
            else:
                break
    def right_boundary(self, root):
        lst = []
        temp = root.right
        while temp:
            if temp.left is not None or temp.right is not None:
                lst.append(temp.data)
            if temp.right is not None:
                temp = temp.right
            elif temp.left is not None:
                temp = temp.left
            else:
                break
        lst.reverse()
        return lst
        
    def inorder(self, root, lst):
        if root:
            self.inorder(root.left, lst)
            if root.left is None and root.right is None:
                lst.append(root.data)
            self.inorder(root.right, lst)
            
    def printBoundaryView(self, root):
        lst=[]
        lst.append(root.data)
        if(root.left is None and root.right is None):
            return lst
        #left boundary excluding leaf node
        self.left_boundary(root,lst)
        
        #getting the leaf node
        self.inorder(root,lst)
        
        #right boundary in reverse order
        lst=lst+self.right_boundary(root)
        return lst
