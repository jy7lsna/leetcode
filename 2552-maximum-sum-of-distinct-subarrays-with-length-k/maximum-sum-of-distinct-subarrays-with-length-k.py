class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        curr_sum = 0
        max_sum = 0
        left = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                curr_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            
            seen.add(nums[right])
            curr_sum += nums[right]

            if len(seen) > k:
                curr_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            
            if len(seen) == k:
                max_sum = max(max_sum, curr_sum)
        
        return max_sum
