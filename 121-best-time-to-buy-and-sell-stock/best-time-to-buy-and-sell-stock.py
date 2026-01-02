class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        max_profit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                profit = price - minPrice
                if profit > max_profit:
                    max_profit = profit
        return max_profit