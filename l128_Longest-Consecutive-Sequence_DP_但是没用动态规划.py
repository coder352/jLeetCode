#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# For example,
#     Given [100, 4, 200, 1, 3, 2],
#     The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# Your algorithm should run in O(n) complexity.
##################################################################
## Solution
# 没用 DP 的思想
# Simple O(n) with Explanation - Just walk each streak
# First turn the input into a set of numbers. That takes O(n) and then we can ask in O(1) whether we have a certain number.
# Then go through the numbers. If the number x is the start of a streak (i.e., x-1 is not in the set), then test y = x+1, x+2, x+3, ...
#     and stop at the first number y not in the set. The length of the streak is then simply y-x and we update our global best with that.
#     Since we check each streak only once, this is overall O(n). This ran in 44 ms on the OJ, one of the fastest Python submissions.
class Solution:
    def longestConsecutive(self, nums):
        nums, best = set(nums), 0  # O(n)
        for x in nums:  # O(n)
            if x - 1 not in nums:  # 内部 hashMap, O(1)
                y = x + 1
                while y in nums: y += 1  # O(1)
                best = max(best, y - x)
        return best
print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
