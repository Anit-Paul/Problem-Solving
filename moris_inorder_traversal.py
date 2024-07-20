class Solution(object):
    def inorderTraversal(self, root):
        cur=root
        res=[]
        while cur:
            if(cur.left==None):
                res.append(cur.val)
                cur=cur.right
            else:
                temp=cur.left
                while(temp.right and temp.right!=cur):
                    temp=temp.right
                if(temp.right is None):
                    temp.right=cur
                    cur=cur.left
                else:
                    temp.right=None
                    res.append(cur.val)
                    cur=cur.right
        return res
