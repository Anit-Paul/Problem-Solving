class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def preorder(self,root,map,idx,level):
        if root is not None:
            if idx not in map:
                map[idx]={}
            if level not in map[idx]:
                map[idx][level]=[]
                map[idx][level].append(root.data)
                
            self.preorder(root.left,map,idx-1,level+1)
            self.preorder(root.right,map,idx+1,level+1)
            
    def topView(self,root):
        map={}
        self.preorder(root,map,0,0)
        lst=[]
        map=sorted(map.items())
        for key,value in map:
            v=min(value.keys())
            lst+=value[v]
        return lst
