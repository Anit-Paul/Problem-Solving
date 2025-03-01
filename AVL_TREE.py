class Node:
    def __init__(self,data):
        self.data=data
        self.height=1
        self.left=None
        self.right=None

class AVL:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        self.root=self.__append(self.root,data)
    
    def __get_height(self,root):
        if root:
            return root.height
        return 0
    
    def __right_rotation(self,root):
        temp=root.left
        root.left=temp.right
        temp.right=root
        root.height=1+max(self.__get_height(root.left),self.__get_height(root.right))
        temp.height=1+max(self.__get_height(temp.left),self.__get_height(temp.right))
        return temp
    
    def __left_rotation(self,root):
        temp=root.right
        root.right=temp.left
        temp.left=root
        root.height=1+max(self.__get_height(root.left),self.__get_height(root.right))
        temp.height=1+max(self.__get_height(temp.left),self.__get_height(temp.right))
        return temp
        
    def __get_balance(self,root):
        left=self.__get_height(root.left)
        right=self.__get_height(root.right)
        return left-right
    
    def __append(self,root,data):
        if root==None:
            return Node(data)
        if root.data>data:
            root.left=self.__append(root.left,data)
        elif root.data<data:
            root.right=self.__append(root.right,data)
        else:
            return root
            
        #storing the height
        root.height=1+max(self.__get_height(root.left),self.__get_height(root.right))
        #check for balancing
        balance=self.__get_balance(root)
        #left-left,left-right
        if balance>1:
            if data<root.left.data: #left left case
                #right rotation
                return self.__right_rotation(root)
            else: #left right case
                root.left=self.__left_rotation(root.left)
                return self.__right_rotation(root)
        #right-right,right-left
        elif balance<-1:
            if data>root.right.data: #right right case
                return self.__left_rotation(root)
            else: #right left case
                root.right=self.__right_rotation(root.right)
                return self.__left_rotation(root)
                
        return root #duplicate elements are not allowed
    
    def inorder(self):
        self.__print_inorder(self.root)
    
    def __print_inorder(self,root):
        if root:
            self.__print_inorder(root.left)
            print(root.data,root.height)
            self.__print_inorder(root.right)

def main():
    tree=AVL()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.inorder()
    
    
if __name__=='__main__':
    main()
    
