class Solution(object):
    def flatten(self, root):
        if root is None:
            return None
        link_list=TreeNode(0)
        res=link_list
        cur=root
        while cur:
            if(cur.left is None):
               link_list.right=TreeNode(cur.val)
               link_list.left=None
               link_list=link_list.right
               cur=cur.right
            else:
                temp=cur.left
                while(temp.right!=None and temp.right!=cur):
                    temp=temp.right
                if(temp.right==None):
                    temp.right=cur
                    link_list.right=TreeNode(cur.val)
                    link_list.left=None
                    link_list=link_list.right
                    cur=cur.left
                else:
                    temp.right=None
                    cur=cur.right
        root.left=None
        root.right=res.right.right
