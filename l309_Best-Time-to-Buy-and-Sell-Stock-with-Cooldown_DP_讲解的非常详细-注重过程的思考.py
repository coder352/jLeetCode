#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# Say you have an array for which the i_th element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
#     (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:
#     prices = [1, 2, 3, 0, 2]
#     maxProfit = 3
#     transactions = [buy, sell, cooldown, buy, sell]
# Credits:
#     Special thanks to @dietpepsi for adding this problem and creating all test cases.
##################################################################
## Solution 1
# free is the maximum profit I can have while being free to buy.
# have is the maximum profit I can have while having stock.
# cool is the maximum profit I can have while cooling down.

# Let me just expand what StefanPochmann explained a little bit:
# free is the maximum profit I can have while being free to buy. I am free to buy in the current iteration either because
#     I was free to buy in the previous iteration and did nothing in the current iteration, or I was cooling down in the previous iteration
#     and did nothing in the current iteration.
# have is the maximum profit I can have while having stock, i.e., I've bought a stock and haven't sold it yet. This happens when
#     I was already holding stock but did not sell in this iteration, or I was free to buy stock last iteration and bought the stock
#     in the current iteration.
# cool is the maximum profit I can have while cooling down. This only happens if I was holding a stock in the previous iteration and
#     sold it in the current iteration.
class Solution:
    def maxProfit(self, prices):
        free = 0
        have = cool = float('-inf')
        for p in prices:
            free, have, cool = max(free, cool), max(have, free - p), have + p
        return max(free, cool)
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
##################################################################
## Solution 2: 更加详细的介绍 [leetcode](https://discuss.leetcode.com/topic/30421/share-my-thinking-process)
# The series of problems are typical dp. The key for dp is to find the variables to represent the states and deduce the transition function.
# Of course one may come up with a O(1) space solution directly, but I think

#     ** it is better to be generous when you think and be greedy when you implement. **

# The natural states for this problem is the 3 possible transactions : buy, sell, rest. Here rest means no transaction on that day (aka cooldown).
# Then the transaction sequences can end with any of these three states.
# For each of them we make an array, buy[n], sell[n] and rest[n].
#     buy[i] means before day i what is the maxProfit for any sequence end with buy.
#     sell[i] means before day i what is the maxProfit for any sequence end with sell.
#     rest[i] means before day i what is the maxProfit for any sequence end with rest.
# Then we want to deduce the transition functions for buy sell and rest. By definition we have:
#     buy[i]  = max(rest[i-1]-price, buy[i-1])
#     sell[i] = max(buy[i-1]+price, sell[i-1])
#     rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
# Where price is the price of day i. All of these are very straightforward. They simply represents :
#     (1) We have to `rest` before we `buy` and
#     (2) we have to `buy` before we `sell`
# One tricky point is how do you make sure you sell before you buy, since from the equations it seems that [buy, rest, buy] is entirely possible.
# Well, the answer lies within the fact that buy[i] <= rest[i] which means rest[i] = max(sell[i-1], rest[i-1]).
#     That made sure [buy, rest, buy] is never occurred.
# A further observation is that and rest[i] <= sell[i] is also true therefore
#     rest[i] = sell[i-1]
# Substitute this in to buy[i] we now have 2 functions instead of 3:
#     buy[i] = max(sell[i-2]-price, buy[i-1])
#     sell[i] = max(buy[i-1]+price, sell[i-1])
# This is better than 3, but
# we can do even better
#     Since states of day i relies only on i-1 and i-2 we can reduce the O(n) space to O(1). And here we are at our final solution:
class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2: return 0
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)  # 这里用到的 prev_sell 是上上次的
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
