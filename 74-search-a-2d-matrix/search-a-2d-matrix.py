class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        ROW, COL = len(matrix), len(matrix[0])
        top, bot = 0, ROW - 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        l, r = 0, COL - 1
        while l <= r:
            mid = (l + r) // 2
            if target >matrix[row][mid]:
                l = mid + 1 
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False


