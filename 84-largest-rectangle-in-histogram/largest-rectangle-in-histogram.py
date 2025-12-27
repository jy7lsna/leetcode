class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)
        
        n = len(heights)
        while stack:
            h = heights[stack.pop()]
            width = n if not stack else n -  stack[-1] - 1
            max_area = max(max_area, h * width)
        
        return max_area   


