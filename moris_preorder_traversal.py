class Solution(object):
    def preorderTraversal(self, root):
        res=[]
        cur=root
        while cur:
            if(cur.left is None):
                res.append(cur.val)
                cur=cur.right
            else:
                temp=cur.left
                while(temp.right!=None and temp.right!=cur):
                    temp=temp.right
                if(temp.right is None):
                    temp.right=cur
                    res.append(cur.val)
                    cur=cur.left
                else:
                    temp.right=None
                    cur=cur.right
        return res
