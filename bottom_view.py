class Solution:
    def __preorder(self,root,map,idx,level):
        if root is not None:
            if idx not in map:
                map[idx]={}
            if level not in map[idx]:
                map[idx][level]=[]
            map[idx][level].append(root.data)
                
            self.__preorder(root.left,map,idx-1,level+1)
            self.__preorder(root.right,map,idx+1,level+1)
    def bottomView(self, root):
        map={}
        self.__preorder(root,map,0,0)
        lst=[]
        map=sorted(map.items())
        for key,value in map:
            m=max(value.keys())
            lst.append(value[m][-1])
        return lst
