class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res


    def quickSort(self, nums, low, high):
        if low < high:
            pi = self.partition(nums, low, high)
            self.quickSort(nums, 0, pi-1)
            self.quickSort(nums, pi+1, high)
    
    def partition(self, nums, low, high):
        pivot = len(nums) - 1
        i = low - 1

        for j in range(low, high):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]
        return i + 1

