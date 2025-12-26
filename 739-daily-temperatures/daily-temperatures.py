class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res



# 73, 74, 75, 71, 69, 72, 76, 73
# 1   1    1   4   2   1   0   0 

# 30, 40, 50, 60 
# 1    1   1   0




