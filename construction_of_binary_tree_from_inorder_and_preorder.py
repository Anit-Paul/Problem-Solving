class Solution(object):
    def construct_tree(self,preorder,inorder):
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        idx = inorder.index(root_val)
        root.left = self.construct_tree(preorder[1:1+idx], inorder[:idx])
        root.right = self.construct_tree(preorder[1+idx:], inorder[idx+1:])
        return root

    def buildTree(self, preorder, inorder):
        return self.construct_tree(preorder,inorder)
