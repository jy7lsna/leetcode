class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            maxP = max(maxP, prices[r] - prices[l])
        return maxP