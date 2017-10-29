#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one
#     share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock
#     before you buy again).
##################################################################
## Solution
# Basically, if tomorrow's price is higher than today's, we buy it today and sell tomorrow. Otherwise, we don't. Here is the code:
class Solution(object):
    def maxProfit(self, prices):
        return sum([b-a for a, b in zip(prices, prices[1:]) if b-a > 0])  # 和下面效果一样, 但是体现了 去 i,j 化
        # return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))  # 每天都可以多次 买/卖
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 7
print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
