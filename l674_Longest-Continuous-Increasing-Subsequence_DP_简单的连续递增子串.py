#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# Given an unsorted array of integers, find the length of longest continuous increasing subsequence.
# Example 1:
#     Input: [1,3,5,4,7]
#     Output: 3
#     Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
#     Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
# Example 2:
#     Input: [2,2,2,2,2]
#     Output: 1
#     Explanation: The longest continuous increasing subsequence is [2], its length is 1.
#     Note: Length of the array will not exceed 10,000.
##################################################################
## Solution: Time: O(n); Space: O(1)
# A continuous subsequence is essentially a subarray. Hence this question is asking for the longest increasing subarray and
#     I have no idea why the question calls it continuous subsequence to confuse the readers.
# Anyway, we can make one pass of the array and keep track of the current streak of increasing elements, reset it when it does not increase.
class Solution(object):
    def findLengthOfLCIS(self, nums):
        max_len = 0
        for i in range(len(nums)):
            curr = 1  # 当前连续子串的长度
            while i + 1 < len(nums) and nums[i] < nums[i + 1]:
                curr, i = curr + 1, i + 1
            max_len = max(max_len, curr)
        return max_len
print(Solution().findLengthOfLCIS([1, 3, 5, 4, 7]))  # 3
print(Solution().findLengthOfLCIS([]))  # 0
print(Solution().findLengthOfLCIS([1]))  # 1
##################################################################
## DP: 还是 DP 的思想比较好理解
class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums: return 0  # 对于 [] 这种结果为 0
        max_len = 1  # 对于 [1] 这种数据不会进行循环, 所以设置为 1
        dp = [1] * len(nums)  # 表示当前位置的连续子串的局部最长
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]: dp[i] = dp[i - 1] + 1
            else: dp[i] = 1
            max_len = max(max_len, dp[i])
        return max_len
print(Solution().findLengthOfLCIS([1, 3, 5, 4, 7]))  # 3
print(Solution().findLengthOfLCIS([]))  # 0
print(Solution().findLengthOfLCIS([1]))  # 1
