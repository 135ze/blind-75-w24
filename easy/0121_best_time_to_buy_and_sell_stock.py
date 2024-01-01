from typing import List

# 121. Best Time to Buy and Sell Stock
# Array, DP

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# -----------------------------------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge case
        if len(prices) == 1:
            return 0
        # init values
        maxProfit = prices[1] - prices[0]
        curMin = prices[0]
        # check against each price
        for i in range (len(prices)):
            curPrice = prices[i]
            curMin = min(curMin, curPrice)
            maxProfit = max(curPrice - curMin, maxProfit)
        if maxProfit < 0:
            return 0
        else:
            return maxProfit
        
# -----------------------------------------------
# Testcases
        
my_sol = Solution()

prices = [[7,1,5,3,6,4], [7,6,4,3,1]]

for priceList in prices:
    print("max profit: ", my_sol.maxProfit(priceList))