class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid 
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1

# -1, 0, 3, 5, 9, 12
#           l  m   h
# 9