class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {} 
        for i, num in enumerate(numbers):
            wanted_num = target - num
            if wanted_num in seen:
                return [seen[wanted_num] + 1, i+1]
            seen[num] = i

# 2, 3, 4 
# 
