#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
##################################################################
## Solution: DP 这种方法跟 ./l131 中的 DP 方法思想一样, 只是这里没有了存储的开销
# Calculate and maintain 1 DP states:
#     d[i], which is the minCut for s[0..i]
# Once we comes to a s[j..i] is palindrome:
# if j==0, the string s[0..i] is a Pal, minCut is 0, d[i]=0;
# else: the current cut num (first cut s[j..i] and then cut the rest s[0...j]) is 1+d[j],

# compare it to the exisiting minCut num d[i], repalce if smaller.
# d[-1] is the answer.
class Solution(object):
    def minCut(self, s):
        dp = [-1] + [0] * len(s)  # 对与 'a' 这种一个字符的, 答案为 0, 算法中有 +1 的步骤, 所以初始化为 -1
        for i in range(1, len(s)+1):
            dp[i] = min([dp[j]+1 for j in range(i) if s[j:i] == s[j:i][::-1]])  # if 后面是判断 s[j:i] 是否是回文, 好神奇...
        # 不能用下面这一行来代替上面的循环, 因为 [] 生成器中没有办法实时更新 d[i] 的值, 所以结果不正确
        # ./l132 中一行暴力递归是因为用了 递归, 不用记录中间的状态
        # dp = [min([dp[j]+1 for j in range(i) if s[j:i] == s[j:i][::-1]]) for i in range(1, len(s)+1)]
        return dp[-1]
print(Solution().minCut('a'))  # 0
print(Solution().minCut('aab'))  # 1
print(Solution().minCut('leet'))  # 2
