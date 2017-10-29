#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# Say you have an array for which the i_th element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.
##################################################################
## Solution: ./l123 中的方法竟然超时了...; 加上剪枝...
class Solution(object):
    def maxProfit(self, k, prices):
        days = len(prices)
        if days < 2:return 0

        # 加了这段代码专门针对下面那种超时的情况进行剪枝
        max_profit = 0
        if k >= days // 2:
            for i in range(1, days): max_profit += max(prices[i] - prices[i-1], 0)
            return max_profit

        dp = [0] * days  # dp[i] 表示在 prices[i] 时的最大 profit
        for i in range(k):
            min_buyin = prices[0]  # prices[] 是常量, 定值;
            for j in range(1, days):
                dp[j], min_buyin = max(dp[j-1], prices[j] - min_buyin), min(min_buyin, prices[j]-dp[j])
        return dp[-1]
print(Solution().maxProfit(2, [7, 1, 5, 3, 6, 4]))  # 7
print(Solution().maxProfit(2, [7, 6, 4, 3, 1]))  # 0
# 1000000000 [106,373,495,46,359,919,906,440,783,583,784,73,238,701,972,308,165,774,990,675,...]  # 40K 个字符, 1 billion 次购买, 超时了
