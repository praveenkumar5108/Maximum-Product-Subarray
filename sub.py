class Solution:
    def maxProduct(self, nums):
        N = len(nums)
        dp1 = [0] * N
        dp2 = [0] * N
        dp1[0] = dp2[0] = nums[0]
        
        for k in range(1, N):
            if nums[k] > 0:
                dp1[k] = max(dp1[k-1] * nums[k], nums[k])
                dp2[k] = min(dp2[k-1] * nums[k], nums[k])
            else:
                dp1[k] = max(dp2[k-1] * nums[k], nums[k])
                dp2[k] = min(dp1[k-1] * nums[k], nums[k])
        
        return max(dp1)  
