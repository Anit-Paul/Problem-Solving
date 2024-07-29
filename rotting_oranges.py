from collections import deque
class Solution(object):
    def is_safe(self,grid,i,j):
        if(i<0 or i>=len(grid)):
            return False
        if(j<0 or j>=len(grid[i])):
            return False
        if(grid[i][j]!=1):
            return False
        return True
    def compute_operation(self,grid):
        q=deque()
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if(grid[i][j]==2):
                    q.append([i,j])
                    grid[i][j]=0
        count=0
        if(len(q)==0):
            return 0
        while q :
            n=len(q)
            for idx in range(n):
                edge=q.popleft()
                #top
                if(self.is_safe(grid,edge[0]-1,edge[1])):
                    q.append([edge[0]-1,edge[1]])
                    grid[edge[0]-1][edge[1]]=0
                #bottom
                if(self.is_safe(grid,edge[0]+1,edge[1])):
                    q.append([edge[0]+1,edge[1]])
                    grid[edge[0]+1][edge[1]]=0
                #left
                if(self.is_safe(grid,edge[0],edge[1]-1)):
                    q.append([edge[0],edge[1]-1])
                    grid[edge[0]][edge[1]-1]=0
                #right
                if(self.is_safe(grid,edge[0],edge[1]+1)):
                    q.append([edge[0],edge[1]+1])
                    grid[edge[0]][edge[1]+1]=0
            count+=1
        return count-1
        
    def orangesRotting(self, grid):
        count=0
        count=self.compute_operation(grid)
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if(grid[i][j]==1):
                    return -1
        return count
        
