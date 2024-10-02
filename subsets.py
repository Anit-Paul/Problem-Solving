class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(0, (1 << n)):
            lst = []
            for j in range(0, n):
                if i & (1 << j) != 0:
                    lst.append(nums[j])
            res.append(lst)
        return res
