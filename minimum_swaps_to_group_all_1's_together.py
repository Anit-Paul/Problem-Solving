class Solution(object):
    def minSwaps(self, nums):
        #count the number of 1's
        c1=0
        for i in nums :
            if i==1:
                c1+=1
        #for maintaining the circular case
        for i in range(0,c1-1):
            nums.append(nums[i])

        #keep count of 0's in every subarray
        c0=0
        i=0
        j=i+c1
        while i<j:
            if(nums[i]==0):
                c0+=1
            i+=1
        mini=c0
        temp=mini
        # now check for every c1 size subarray
        n=len(nums)-c1+1
        for i in range(1,n):
            j=i+c1-1
            if(nums[i-1]==0):
                temp-=1
            if(nums[j]==0):
                temp+=1
            mini=min(mini,temp)
        
        return mini

        
