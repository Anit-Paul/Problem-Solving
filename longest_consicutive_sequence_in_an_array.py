class Solution(object):
    def longestConsecutive(self, nums):
        ans=0
        res=0
        nums=set(nums)
        for num in nums :
            if num-1 not in nums :
                res=1
                current=num
                while current+1 in nums:
                    res+=1
                    current+=1
            ans=max(ans,res)
        return ans
