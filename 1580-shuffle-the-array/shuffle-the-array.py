class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        i, j = 0, n

        while i < n and i < 2 * n:
            res.append(nums[i])
            res.append(nums[j])
            i += 1
            j += 1
        return res