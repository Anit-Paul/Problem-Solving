class Solution(object):
    def inorder(self,root,idx,map,level):
        if(root is not None):
            self.inorder(root.left,idx-1,map,level+1)
            if idx not in map:
                map[idx]={}
            if level not in map[idx]:
                map[idx][level]=[]
            map[idx][level].append(root.val)
            self.inorder(root.right,idx+1,map,level+1)
    def verticalTraversal(self, root):
        map={}
        self.inorder(root,0,map,0)
        res=[]
        map=sorted(map.items())
        for key,values in map:
            values=sorted(values.items())
            lst=[]
            for k,v in values:
                s=sorted(v)
                lst+=s
            res.append(lst)
        return res
