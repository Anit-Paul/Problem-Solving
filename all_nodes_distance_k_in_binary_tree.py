from collections import deque
class Solution(object):
    def __get_parents(self,root,parent):
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
    def __get_result(self,root,parent,k):
        visit=[]
        q=deque()
        q.append(root)
        visit.append(root)
        dis=0
        while q:
            if dis==k:
                break
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
        res=[]
        while q:
            res.append(q.popleft().val)
        return res
    def distanceK(self, root, target, k):
        parent={}
        self.__get_parents(root,parent)
        return self.__get_result(target,parent,k)
