class Solution(object):
    @staticmethod
    def __inorder(root,k):
        while root:
            if(root.left==None):
                k-=1
                if(k==0):
                    return root.val
                root=root.right
            else:
                temp=root.left
                while(temp.right!=None and temp.right!=root):
                    temp=temp.right
                if temp.right:
                    temp.right=None
                    k-=1
                    if(k==0):
                        return root.val
                    root=root.right
                else:
                    temp.right=root
                    root=root.left
        return None
    def kthSmallest(self, root, k):
        return self.__inorder(root,k)
