class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])
        low=0
        high=(m*n)-1
        while(low<=high):
            mid=(low+high)//2
            if(matrix[mid/n][mid%n]==target):
                return True
            elif(matrix[mid/n][mid%n]>target):
                high=mid-1
            else:
                low=mid+1
        return False
        
