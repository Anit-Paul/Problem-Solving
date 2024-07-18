#Brute fource
lass Solution(object):
    def get_path(self,root,p,path):
        if root is None:
            return False
        path.append(root)
        if(root==p):
            return True
        left=False
        right=False
        if(root.left is not None):
            left=self.get_path(root.left,p,path)
        if left:
            return True
        if(root.right is not None):
            right=self.get_path(root.right,p,path)
        if right:
            return True
        path.pop()
            
            
    def lowestCommonAncestor(self, root, p, q):
        path1=[]
        path2=[]
        self.get_path(root,p,path1)
        self.get_path(root,q,path2)
        res=None
        for i in path1:
            if i in path2:
                res=i
        return res

#optimised 
class Solution(object):
    def __get_result(self,root,p,q):
        if(root==p):
            return p
        if(root==q):
            return q
        if(root is None):
            return None
        left=self.__get_result(root.left,p,q)
        right=self.__get_result(root.right,p,q)
        if(left is None):
            return right
        if(right is None):
            return left
        else:
            return root

    def lowestCommonAncestor(self, root, p, q):
        return self.__get_result(root,p,q)
