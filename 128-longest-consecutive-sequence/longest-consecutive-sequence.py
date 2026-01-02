class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
        

# 100, 4, 200, 1, 3, 2
#  i
# 2, 3, 1, 4