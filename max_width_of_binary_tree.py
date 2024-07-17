class Solution(object):
    def __helper(self,root,map,idx,level):
        if root is not None:
            self.__helper(root.left,map,2*idx+1,level+1)
            if level not in map:
                map[level]=[]
            map[level].append(idx)
            self.__helper(root.right,map,2*idx+2,level+1)

    def widthOfBinaryTree(self, root):
        map={}
        lst=[]
        if root is None:
            return 0
        self.__helper(root,map,0,0)
        for key,value in map.items():
            lst.append(max(value)-min(value)+1)
        return max(lst)
