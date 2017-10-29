#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# Say you have an array for which the i_th element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
##################################################################
## Solution
# Solution is commented in the code. Time complexity is O(kn), space complexity can be O(n) because this DP only uses the result from last step.
#     But for cleaness this solution still used O(kn) space complexity to preserve similarity to the equations in the comments.
# 状态转移方程:
#     f[k, ii] represents the max profit up until prices[ii] (Note: NOT ending with prices[ii]) using at most k transactions.
#     f[k, ii] = max(f[k, ii-1], prices[ii] - prices[jj] + f[k-1, jj]) { jj in range of [0, ii-1] }
#              = max(f[k, ii-1], prices[ii] + max(f[k-1, jj] - prices[jj]))
#     f[0, ii] = 0; 0 times transation makes 0 profit
#     f[k, 0]  = 0; if there is only one price data point you can't make any money no matter how many times you can trade
# I understand that the first option is "do nothing" and the second option is "sell at ii while buy at jj";
# I think f[k-1, jj] is correct, since f[k-1, jj] means the maximum profit up until jj with at most k-1 transactions completed and
#     this means you will buy at jj and then sell at ii.
# CPP Code:
#     class Solution {
#     public:
#         int maxProfit(vector<int> &prices) {
#             if (prices.size() <= 1) return 0;
#             else {
#                 int K = 2; // number of max transation allowed
#                 int maxProf = 0;
#                 vector<vector<int>> f(K+1, vector<int>(prices.size(), 0));
#                 for (int kk = 1; kk <= K; kk++) {
#                     int tmpMax = f[kk-1][0] - prices[0];
#                     for (int ii = 1; ii < prices.size(); ii++) {
#                         f[kk][ii] = max(f[kk][ii-1], prices[ii] + tmpMax);
#                         tmpMax = max(tmpMax, f[kk-1][ii] - prices[ii]);
#                         maxProf = max(f[kk][ii], maxProf);
#                     }
#                 }
#                 return maxProf;
#             }
#         }
#     };
##################################################################
## 上面开的空间很大, 这里是优化版的
#     f[k, ii] = max(f[k, ii-1], prices[ii] - prices[jj] + f[k-1, jj]) { jj in range of [0, ii-1] }
#              = max(f[k, ii-1], prices[ii] + max(f[k-1, jj] - prices[jj]))
#              = max(f[k, ii-1], prices[ii] - min(prices[jj] - f[k-1, jj]))
#              = max(f[ii-1], prices[ii] - min(prices[jj] - f[jj]))  # See code below!
class Solution(object):
    def maxProfit(self, prices):  # 这里不能随便加参数, 所以新写了一个函数
        return self.maxProfitMultiple(prices, 2)
    def maxProfitMultiple(self, prices, times):
        days = len(prices)
        if days < 2:return 0
        dp = [0] * days  # dp[i] 表示在 prices[i] 时的最大 profit
        for i in range(times):
            min_buyin = prices[0]  # prices[] 是常量, 定值;
            for j in range(1, days):
                dp[j], min_buyin = max(dp[j-1], prices[j] - min_buyin), min(min_buyin, prices[j]-dp[j])
        return dp[-1]
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 7
print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
