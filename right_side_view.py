class Solution(object):
    def inorder(self,root,level,map):
        if root is not None:
            self.inorder(root.left,level+1,map)
            if(level not in map):
                map[level]=0
            map[level]=root.val
            self.inorder(root.right,level+1,map)
    def rightSideView(self, root):
        map={}
        self.inorder(root,0,map)
        map=sorted(map.items())
        lst=[]
        for key,value in map:
            lst.append(value)
        return lst
