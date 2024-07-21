class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class bst:
    def __init__(self):
        self.__root=None
    def inorder(self):
        self.__cls_inorder(self.__root)
        
    def __cls_inorder(self,root):
        res=[]
        while root:
            if(root.left is None):
                res.append(root.val)
                root=root.right
            else:
                temp=root.left
                while(temp.right!=None and temp.right!=root):
                    temp=temp.right
                if temp.right:
                    temp.right=None
                    res.append(root.val)
                    root=root.right
                else:
                    temp.right=root
                    root=root.left
        print("the in order traversal is "+str(res))
            
    
    def insert(self,val):
        self.__root=self.__insert_node(self.__root,val)
        
    @staticmethod
    def __insert_node(root,val):
        if root is None:
            root=Node(val)
        elif root.val>val:
            root.left=bst.__insert_node(root.left,val)
        elif root.val<val:
            root.right=bst.__insert_node(root.right,val)
        return root
    
    def search(self,val):
        return self.__cls_search(self.__root,val)
    @staticmethod
    def __cls_search(root,val):
        if(root is None):
            return False
        if(root.val==val):
            return True
        if root.val>val:
            return bst.__cls_search(root.left,val)
        elif root.val<val:
            return bst.__cls_search(root.right,val)
    def delete(self,val):
        self.root=self.__delete_node(self.__root,val)    
        
    @staticmethod
    def __delete_node(root,val):
        if root is None:
            return None
        if root.val>val:
            root.left=bst.__delete_node(root.left,val)
        elif root.val<val:
            root.right=bst.__delete_node(root.right,val)
        else:
            #for leaf node
            if(root.left==None and root.right==None):
                return None
            #for 1 child
            if(root.left==None):
                return root.right
            if(root.right==None):
                return root.left
            #for 2 children
            temp=bst.__inorder_successor(root.right)
            root.val=temp.val
            root.right=bst.__delete_node(root.right,val)
def main():
    a=bst()
    a.insert(2)
    a.insert(3)
    a.insert(1)
    a.insert(20)
    a.insert(0)
    a.insert(12)
    a.inorder()
    print(a.search(200))
    a.delete(3)
    a.inorder()

if __name__=='__main__':
    main()
