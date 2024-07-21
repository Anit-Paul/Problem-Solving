class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        sum_count = {0: 1}
        cum_sum = 0 
        
        for num in nums:
            cum_sum += num 
            
            
            if cum_sum - k in sum_count:
                count += sum_count[cum_sum - k]
                
            
            if cum_sum in sum_count:
                sum_count[cum_sum] += 1
            else:
                sum_count[cum_sum] = 1
        print(sum_count)
        
        return count
