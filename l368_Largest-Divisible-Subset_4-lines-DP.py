#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
#     Si % Sj = 0 or Sj % Si = 0.
# If there are multiple solutions, return any subset is fine.

# Example 1:
# nums: [1, 2, 3]
# Result: [1, 2] (of course, [1, 3] will also be ok)
# Example 2:
# nums: [1, 2, 4, 8]
# Result: [1, 2, 4, 8]
##################################################################
## Solution; 参考题目后面大神的代码
# 思路: 其实和求最大上升子序列 LIS 差不多, 只不过这题要求输出序列而已.
# 先把数组排好序. 首先要明确, 若 a<b 且 b%a==0 ,  b <c 且 c%b==0 那么必然有 c%a==0
# 我们设 dp[i] 为最大的子集长度, 更新的时候保存上一个的下标即可.
# For an increasingly sorted array of integers a[1 .. n]
# T[n] = the length of the largest divisible subset whose largest number is a[n]
# T[n+1] = max{ 1 + T[i] if a[n+1] mod a[i] == 0 else 1 }
# Now, deducting T[n] becomes straight forward with a DP trick. For the final result we will need to maintain a backtrace array for the answer.
#     Or, we can save the middle process with more space.
class Solution:
    def largestDivisibleSubset(self, nums):
        S = {-1: set()}  # 这里的初始化做的也很好...; x % -1 恒为 0, 所以下面的 max() 不会报错...
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}  # 这动态规划写的..., 满分; | {x} 是 set() 添加元素的另一种方式
        return sorted(list(max(S.values(), key=len)))
print(Solution().largestDivisibleSubset([1, 2, 4, 8]))
# My S[x] is the largest subset with x as the largest element, i.e., the subset of all divisors of x in the input.
# With S[-1] = emptyset as useful base case.
# Since divisibility is transitive, a multiple x of some divisor d is also a multiple of all elements in S[d],
#     so it's not necessary to explicitly test divisibility of x by all elements in S[d]. Testing x % d suffices.
# While storing entire subsets isn't super efficient, it's also not that bad. To extend a subset, the new element must be divisible
#     by all elements in it, meaning it must be at least twice as large as the largest element in it. So with the 31-bit integers
##################################################################
## Summary
# 1. 这里用了很多的内存, 是因为输出结果要包含动态规划的中间步骤;
# 2. 当然也可以建立一个 step[] 数组, step[i] 表示 nums[i] 对应的 上一个数的 index;
#    实现起来不难, 只是不好看了...; 因为在计算完当前的 nums[i] 后, nums[:i] 的状态就已经完全确定了, 不会再发生变化
