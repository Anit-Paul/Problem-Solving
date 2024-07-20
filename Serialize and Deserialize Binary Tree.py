from collections import deque
class Codec:

    def serialize(self, root):
        q=deque()
        q.append(root)
        s=''
        while q:
            current=q.popleft()
            if current:
                q.append(current.left)
                q.append(current.right)
                s=s+str(current.val)+' '
            else:
                s=s+'#'+' '
    
        return s[:len(s)-1]
        
    def construct_tree(self,data):
        token=data.split(' ')
        q=deque()
        if(not data or token[0]=='#'):
            return None
        root=TreeNode(int(token.pop(0)))
        q.append(root)
        while q:
            node=q.popleft()
            left=token.pop(0)
            if left!='#':
                node.left=TreeNode(int(left))
                q.append(node.left)
            right=token.pop(0)
            if right!='#':
                node.right=TreeNode(int(right))
                q.append(node.right)

        return root

    def deserialize(self, data):
        idx=0
        return self.construct_tree(data)
