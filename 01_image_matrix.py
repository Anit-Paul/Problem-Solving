from collections import deque
class temp:
    def __init__(self,i,j,wt):
        self.i=i
        self.j=j
        self.wt=wt


class Solution(object):
    def is_safe(self,i,j,visit,m,n):
        if(i<0 or i>=m):
            return False
        if(j<0 or j>=n):
            return False
        if(visit[i][j]==1):
            return False
        return True
    def updateMatrix(self, mat):
        m=len(mat)
        n=len(mat[0])
        visit=[[0 for _ in range(n)] for _ in range(m)]
        res=[[0 for _ in range(n)] for _ in range(m)]
        q=deque()
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==0):
                    visit[i][j]=1
                    q.append(temp(i,j,0))
        while q:
            my_temp=q.popleft()
            #top
            if self.is_safe(my_temp.i-1,my_temp.j,visit,m,n):
                visit[my_temp.i-1][my_temp.j]=1
                q.append(temp(my_temp.i-1,my_temp.j,my_temp.wt+1))
            #bottom
            if self.is_safe(my_temp.i+1,my_temp.j,visit,m,n):
                visit[my_temp.i+1][my_temp.j]=1
                q.append(temp(my_temp.i+1,my_temp.j,my_temp.wt+1))
            #left
            if self.is_safe(my_temp.i,my_temp.j-1,visit,m,n):
                visit[my_temp.i][my_temp.j-1]=1
                q.append(temp(my_temp.i,my_temp.j-1,my_temp.wt+1))
            #right
            if self.is_safe(my_temp.i,my_temp.j+1,visit,m,n):
                visit[my_temp.i][my_temp.j+1]=1
                q.append(temp(my_temp.i,my_temp.j+1,my_temp.wt+1))
            #updating in result
            res[my_temp.i][my_temp.j]=my_temp.wt

        return res
        
