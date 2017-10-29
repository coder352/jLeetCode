#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# Given an unsorted array of integers, find the number of longest increasing subsequence.
# Example 1:
#     Input: [1,3,5,4,7]
#     Output: 2
#     Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:
#     Input: [2,2,2,2,2]
#     Output: 5
#     Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
# Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
##################################################################
## Solution: 先根据 ./l300 写一个错误的, 说明不能用 NlogN 的复杂度来找了...
class Solution:
    def lengthOfLIS(self, nums):
        import bisect
        minend = [float('inf')] * (len(nums) + 1)  # minend[i] is the minimum ending of an increasing subsequence of length i+1
        count = [0] * len(nums)
        for num in nums:
            count[bisect.bisect_left(minend, num)] += 1
            minend[bisect.bisect_left(minend, num)] = num
        return count[minend.index(float('inf')) - 1]  # 找到第一个 inf, 好厉害...
print(Solution().lengthOfLIS([1, 3, 5, 4, 7]))  # 1; 因为 只能找到 [1, 3, 4, 7], [1, 3, 5, 7] 已经找不到了
print(Solution().lengthOfLIS([2, 2, 2, 2, 2]))  # 5
# 所以要根据 ./l300 中的另一种方法 N^2 的来修改
##################################################################
##
# Well this question is based on problem #300 Longest Increasing Subsequence problem. In problem #300, dp solution is quite easy to come forward, which can be written as follow:
class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp, ans = [1] * len(nums), 1
        for i in range(1,len(nums)):
            dp[i] = max([dp[j]+1 for j in range(i) if nums[i]>nums[j]]+[1])
            ans = max(ans, dp[i])
        return ans
# Here dp[i] represents the length of the longest subsequence in nums[:i+1] && ended with index i. And when I calculate array dp,
#     I just update the result, stored in ans.

# So now let's back to this problem, the biggest difference here is that we also need to find the number of the longest subsequence.
#     A basic idea is to use another array to memorize the number, so the code is as follow:
class Solution(object):
    def findNumberOfLIS(self, nums):
        if not nums: return 0
        dp1, dp2 = [1] * len(nums), [1] *len(nums)
        count, maxval = 1, 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp1[j] + 1 > dp1[i]: dp1[i], dp2[i] = dp1[j] + 1, dp2[j]
                    elif dp1[j] + 1 == dp1[i]: dp2[i] += dp2[j]
            if dp1[i] > maxval: maxval, count = dp1[i], dp2[i]
            elif dp1[i] == maxval: count += dp2[i]
        return count
print(Solution().findNumberOfLIS([1, 3, 5, 4, 7]))  # 2
print(Solution().findNumberOfLIS([2, 2, 2, 2, 2]))  # 5
# dp1 works the same as dp in problem #300: it represents the length of the longest subsequence in nums[:i+1] && ended with index i.
# dp2 represents the number of the subsequences which are satisfied the conditions mentioned in above.
# And also as problem #300, I also update the final result, stored in count in the loop.
# maxval represents the length of the longest increasing subsequence.
# count represents the number of the increasing subsequence with length equals to maxval.
# The time complexity is O(n^2)---time,O(n)---space.
