class Solution(object):
    def is_safe(self,grid,i,j):
        if(i<0 or i>=len(grid)):
            return False
        if(j<0 or j>=len(grid[0])):
            return False
        if(grid[i][j]==0):
            return False
        return True
    def update(self,grid,i,j):
        grid[i][j]=0
        #top
        if(self.is_safe(grid,i-1,j)):
            self.update(grid,i-1,j)
        #bottom
        if(self.is_safe(grid,i+1,j)):
            self.update(grid,i+1,j)
        #left
        if(self.is_safe(grid,i,j-1)):
            self.update(grid,i,j-1)
        #right
        if(self.is_safe(grid,i,j+1)):
            self.update(grid,i,j+1)
    def numEnclaves(self, grid):
        #top row
        for j in range(len(grid[0])):
            if(grid[0][j]==1):
                self.update(grid,0,j)
        #bottom row
        for j in range(len(grid[0])):
            if(grid[len(grid)-1][j]==1):
                self.update(grid,len(grid)-1,j)
        #left most
        for i in range(len(grid)):
            if(grid[i][0]==1):
                self.update(grid,i,0)
        #right most
        for i in range(len(grid)):
            if(grid[i][len(grid[0])-1]==1):
                self.update(grid,i,len(grid[0])-1)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j]==1):
                    count+=1
        return count
        
