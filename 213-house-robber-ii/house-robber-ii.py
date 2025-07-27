class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(arr):
            dp0, dp1 = 0, 0
            for n in arr:
                dp0, dp1 =  dp1, max(dp1, dp0 + n)
            return dp1
        
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))