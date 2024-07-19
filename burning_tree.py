from collections import deque
class Solution:
    def __get_parent(self,root,parent):
        q=deque()
        q.append(root)
        parent[root]=root
        while q:
            current=q.popleft()
            if current.left:
                q.append(current.left)
                parent[current.left]=current
            if current.right:
                q.append(current.right)
                parent[current.right]=current
    def __get_result(self,root,parent):
        visit=[]
        q=deque()
        q.append(root)
        visit.append(root)
        dis=0
        while q:
            size=len(q)
            for i in range (0,size):
                current=q.popleft()
                if current.left:
                    if current.left not in visit:
                        q.append(current.left)
                        visit.append(current.left)
                if current.right:
                    if current.right not in visit:
                        q.append(current.right)
                        visit.append(current.right)
                if parent[current] not in visit:
                    q.append(parent[current])
                    visit.append(parent[current])
            dis+=1
        return dis-1
    def minTime(self, root,target):
        # code here
        parent={}
        self.__get_parent(root,parent)
        t=None
        for key,value in parent.items():
            if(key.data==target):
                t=key
                break
        return self. __get_result(t,parent)
