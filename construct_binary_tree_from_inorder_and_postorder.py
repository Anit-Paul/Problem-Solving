class Solution(object):
    def __construct_tree(self,inorder,postorder):
        if len(inorder)==0 or len(postorder)==0:
            return None
        root_val=postorder[-1]
        root=TreeNode(root_val)
        idx=inorder.index(root_val)
        root.left=self.__construct_tree(inorder[:idx],postorder[:idx])
        root.right=self.__construct_tree(inorder[idx+1:],postorder[idx:-1])
        return root
    def buildTree(self, inorder, postorder):
        return self.__construct_tree(inorder,postorder)
