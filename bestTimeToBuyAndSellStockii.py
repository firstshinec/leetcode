# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

# do not buy it when price decreases continuously. buy it when the prices reaches locally minimum
# do not sell it when prices increases continuouly. sell it when the prices reaches locally maximum or in the last day
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        
        max_profit = 0
        idx = 0
        cost = prices[0]
        status = 1 #0:buy, 1:sell
        for i in range(len(prices)-1):
            if status == 0:
                if prices[i+1] > prices[i]:
                    cost = prices[i]
                    status = 1
            if status == 1:
                if prices[i+1] < prices[i]:
                    max_profit += prices[i] - cost
                    cost = prices[i+1]
                    status = 0
                elif i+2 == len(prices): #the last day and the price keeps rising
                    max_profit += prices[i+1] - cost
        return max_profit