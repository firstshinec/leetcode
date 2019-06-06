# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        
        min_buy = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > min_buy:
                max_profit = max(max_profit, prices[i] - min_buy)
            else:
                min_buy = prices[i]
        return max_profit