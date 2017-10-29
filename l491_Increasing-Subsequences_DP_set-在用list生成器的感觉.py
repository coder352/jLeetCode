#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# Given an integer array, your task is to find all the different possible increasing subsequences of the given array,
#     and the length of an increasing subsequence should be at least 2 .
# Example:
#     Input: [4, 6, 7, 7]
#     Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# Note:
#     The length of the given array will not exceed 15.
#     The range of integer in the given array is [-100,100].
#     The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
##################################################################
## Solution
# First build all increasing subsequences regardless of length, then filter out the too short ones.
class Solution:
    def findSubsequences(self, nums):
        subs = {()}
        for num in nums:
            subs |= {sub + (num,) for sub in subs if not sub or sub[-1] <= num}
        return [sub for sub in subs if len(sub) >= 2]
print(Solution().findSubsequences([4, 6, 7, 7]))
