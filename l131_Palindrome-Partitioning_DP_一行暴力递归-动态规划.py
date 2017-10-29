#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
# For example, given s = "aab",
# Return
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
##################################################################
## Solution: 一行暴力
class Solution:
    def partition(self, s):
        # return [[s[:i]] + rest for i in range(1, len(s)+1) if s[:i] == s[i-1::-1] for rest in self.partition(s[i:])] or [[]]  # 这里的 or 是整个 return 层面的
        return [[s[:i]] + rest for i in range(1, len(s)+1) if s[:i] == s[:i][::-1] for rest in self.partition(s[i:])] or [[]]  # 这里的 or 是整个 return 层面的
print(Solution().partition('aab'))  # 上面只是修改了求回文串的方式..., 好神奇
##################################################################
## DFS: recursive/iterative backtracking solution 递归回溯; 和上面的一行暴力一样
class Solution:
    isPal = lambda x: x == x[::-1]
    def partition(self, s):
        if not s: return [[]]  # 因为是 + rest, 先是 for rest in [[]], 去掉最外面的 []; 然后 + rest 相当于 + [] 在去掉一层 [], 就什么也没有了
        res = []
        for i in range(1, len(s) + 1):
            if Solution.isPal(s[:i]):
                # res.append([[s[:i]] + rest for rest in self.partition(s[i:])])  # 用 append 的结果很奇怪...
                res += [[s[:i]] + rest for rest in self.partition(s[i:])]  # + 会把外层的 [] 去掉, 恰好这里的 list 生成器也带 []
        return res  # 也可以用下面那句话代替 for 循环, 这样就相当于上面 一行暴力 的方法
        # return [[s[:i]] + rest for i in range(1, len(s)+1) if Solution.isPal(s[:i]) for rest in self.partition(s[i:])]
print(Solution().partition('aab'))
##################################################################
## DP: 上面的 DFS 时间复杂度和大 O(n!), 可以进行剪枝, 其实剪完枝以后也就是 DP 了
# Use a DP vecor DP[i] to record all solutions using string s[:i+1]
# 使用 DP 算法以后一般就没有 递归 的步骤了, (树型DP 除外)
# 状态转移方程: DP[i] = {DP[j] + str[j:i]} if str[j:i] pallindrome; 下面的解释更专业
# Calculate and maintain 1 DP states:
#     d[i]: which is the all palindrome of s[0..i]
# Once we comes to a s[j..i] is palindrome:
# d[i] = d[j] + s[j:i]
class Solution:
    isPalindrome = lambda x: x == x[::-1]
    def partition(self, s):
        if not s: return [[]]
        dp = {0:[[]], 1:[[s[0]]]}  # dp[i] 里面存放的就是 一个个双层 list 嵌套
        for i in range(1, len(s)):
            dp[i+1] = []
            for j in range(0, i+1):
                if Solution.isPalindrome(s[j:i+1]):
                    for sol in dp[j]:  # 这里的 sol 相当于上面暴力递归中可以进行的 记忆化剪枝的过程
                        dp[i+1].append(sol + [s[j:i+1]])  # sol 是 ['str', 'str'](因为有 for sol in), [s[j:i+1]] 运算时也会去掉 [], append() 刚好又不用 []
        return dp[len(s)]
print(Solution().partition('aab'))
