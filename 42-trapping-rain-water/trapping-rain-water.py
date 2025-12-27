class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                mid = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                h = min(height[left], height[i]) - height[mid]
                w = i - left - 1
                water += h * w
            stack.append(i)
        return water

