#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# Note: This is an extension of House Robber.
# After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention.
#     This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
#     Meanwhile, the security system for these houses remain the same as for those in the previous street.
# Given a list of non-negative integers representing the amount of money of each house,
#     determine the maximum amount of money you can rob tonight without alerting the police.
# Credits:
#     Special thanks to @Freezen for adding this problem and creating all test cases.
##################################################################
## Solution
# Based on the recursive formula(1st House Robber):
# f(0) = nums[0]
# f(1) = max(num[0], num[1])
# f(k) = max(f(k-2) + nums[k], f(k-1))
#
# Basically this problem is the same as the 1st House Robber, except we cannot pick the first if we pick the last and vice versa.
# Thus, let F(i, j) denote the solution for House Robber 1 for houses in range [i, j), House Robber II is defined as:
#     max(F(0, n-1), F(1, n))
class Solution:  # 和 ./l198_House-Robber_3-lines-DP.py 进行对比
    def rob(self, nums):
        if len(nums) == 1: return nums[0]
        def subrob(subnums):
            last, now = 0, 0
            for i in subnums: last, now = now, max(last + i, now)
            return now
        return max(subrob(nums[:-1]), subrob(nums[1:]))
print(Solution().rob([1, 2, 3, 4, 5]))  # 8
print(Solution().rob([1, 1, 1]))  # 1
print(Solution().rob([2, 1]))  # 2
print(Solution().rob([1]))  # 1
