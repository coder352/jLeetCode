#!/usr/bin/python
# coding: utf-8
##################################################################
## Description
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# UPDATE (2016/2/13):
# The return format had been changed to zero-based indices. Please read the above updated description carefully.
##################################################################
## Solution
# 需找出一个列表中是否有两个数的和为一个给定的数, 并返回这两个数的下标.
# 需要用到 python 里面的字典(相当于 hash 表), 判断第 i 个数前面是否有一个数的值为 target - num[i]. 代码如下:
class Solution:
    def twoSum(self, num, target):
        tmp = {}
        for i in range(len(num)):
            if target - num[i] in tmp: return [tmp[target - num[i]], i]
            else: tmp[num[i]] = i
        # 方法二: 比较笨,但容易想到
        # for i in nums:
        #     for j in xrange(nums.index(i) + 1, len(nums)):
        #         if i + nums[j] == target:
        #             return [nums.index(i), j]
if __name__ == '__main__':
    res = Solution()
    print(res.twoSum([2, 7, 11, 15], 9))
