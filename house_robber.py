class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        result=[-float('inf') for _ in range(len(nums))]
        result[len(nums)-1]=nums[len(nums)-1]
        result[len(nums)-2]=nums[len(nums)-2]
        for i in range(len(nums)-1,-1,-1):
            for j in range(2,len(nums)):
                if i+j>=len(nums):
                    break
                result[i]=max(result[i],nums[i]+result[i+j])
        return max(result)
