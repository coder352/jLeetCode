#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm
#     to find the maximum profit.
# Example 1:
#     Input: [7, 1, 5, 3, 6, 4]
#     Output: 5
#     max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
#     Input: [7, 6, 4, 3, 1]
#     Output: 0
#     In this case, no transaction is done, i.e. max profit = 0.
##################################################################
## Solution: one-line; Not DP
class Solution:
    def maxProfit(self, prices):
        from functools import reduce
        # return reduce(lambda (p, l), x: (max(p, x-l), min(l, x)), prices, (0, 1<<33))[0]  # Python2 版本
        return reduce(lambda p, x: (max(p[0], x-p[1]), min(p[1], x)), prices, (0, 1<<33))[0]
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
##################################################################
## The original:
class Solution:
    def maxProfit(self, prices):
        profit, low = 0, 1 << 33  # 到当前为止, 最新利润 和 最低价格
        for price in prices:
            profit = max(profit, price - low)
            low = min(low, price)
        return profit
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
##################################################################
## DP; 但还没上面效果好
# The logic to solve this problem is same as "max subarray problem" using Kadane's Algorithm. Since no body has mentioned this so far,
#     I thought it's a good thing for everybody to know.
# All the straight forward solution should work, but if the interviewer twists the question slightly by giving the difference array of prices,
#     Ex: for {1, 7, 4, 11}, if he gives {0, 6, -3, 7}, you might end up being confused.
# Here, the logic is to calculate the difference (maxCur += prices[i] - prices[i-1]) of the original array, and find a contiguous subarray

# p[i-1] + prices[i] - prices[i-1]
# today's largest income = yesterday's largest income + today's selling money(may a Negative number)
#     giving maximum profit. If the difference falls below 0, reset it to zero.
class Solution:
    def maxProfit(self, prices):
        p = [0]
        for i in range(1, len(prices)): p.append(max(0, p[i-1] + prices[i] - prices[i-1]))
        return max(p)
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
# Find maximum profit when sell at day j. We either hold the stock at day j-1 or not. If hold then the profit is p[j-1] + prices[j] -prices[j-1]. Otherwise it's 0.
