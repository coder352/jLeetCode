#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# Given a string S and a string T, count the number of distinct subsequences of S which equals T.
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters
#     without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
# Here is an example:
#     S = "rabbbit", T = "rabbit"
#     Return 3.
##################################################################
## Solution
# The idea is the following:
# we will build an array mem where mem[i+1][j+1] means that S[0..j] contains T[0..i] that many times as distinct subsequences.
#     Therefor the result will be mem[T.length()][S.length()].
# we can build this array rows-by-rows:
# the first row must be filled with 1. That's because the empty string is a subsequence of any string but only 1 time.
#     So mem[0][j] = 1 for every j. So with this we not only make our lives easier, but we also return correct value if T is an empty string.
# the first column of every rows except the first must be 0. This is because an empty string cannot contain a non-empty string as a substring
#     -- the very first item of the array: mem[0][0] = 1, because an empty string contains the empty string 1 time.
# So the matrix looks like this:
#   S 0123....j
# T +----------+
#   |1111111111|
# 0 |0         |
# 1 |0         |
# 2 |0         |
# . |0         |
# . |0         |
# i |0         |
# From here we can easily fill the whole grid: for each (x, y), we check if S[x] == T[y] we add the previous item and the previous item
#     in the previous row, otherwise we copy the previous item in the same row. The reason is simple:  # 左边和左上角相加
# if the current character in S doesn't equal to current character T, then we have the same number of distinct subsequences as
#     we had without the new character.
# if the current character in S equal to the current character T, then the distinct number of subsequences:
#     the number we had before plus the distinct number of subsequences we had with less longer T and less longer S.
# An example:
# S: [acdabefbc] and T: [ab]
# first we check with a:
#            *  *
#       S = [acdabefbc]
# mem[1] = [0111222222]
# then we check with ab:
#                *  * ]
#       S = [acdabefbc]
# mem[1] = [0111222222]
# mem[2] = [0000022244]
# And the result is 4, as the distinct subsequences are:
#       S = [a   b    ]
#       S = [a      b ]
#       S = [   ab    ]
#       S = [   a   b ]

# Recurrence relation:
#     dp[i][j] = dp[i - 1][j] + (dp[i - 1][j - 1] if s[i - 1] == t[j - 1])
class Solution(object):
    def numDistinct(self, s, t):
        dp = [[1] * (len(s)+1)] + [[0] * (len(s)+1) for y in range(len(t))]
        for j in range(1, len(t)+1):
            for i in range(1, len(s)+1):
                dp[j][i] += dp[j-1][i-1] + dp[j][i-1] if s[i-1] == t[j-1] else dp[j][i-1]
        return dp[-1][-1]
print(Solution().numDistinct('rabbbit', 'rabbit'))  # 3
##################################################################
## Space optimization
# The states are only from top and left-top. Thus, 1-D array is enough and uses some temp variables to roll the array all the way down.
class Solution(object):
    def numDistinct(self, s, t):
        dp = [1] + [0] * len(t)
        for i in range(1, len(s) + 1):
            pre = dp[0]
            for j in range(1, len(t) + 1):
                pre, dp[j] = dp[j], dp[j] + pre * (s[i - 1] == t[j - 1])  # represent the three lines below; 这里的 pre 值得是 dp[i-1][j-1]
        return dp[-1]
print(Solution().numDistinct('rabbbit', 'rabbit'))  # 3
                # tmp = dp[j]
                # dp[j] = dp[j] + pre * (s[i - 1] == t[j - 1])
                # pre = tmp
##################################################################
## 从暴力递归 -> 记忆化搜索 -> 动态规划
# ``` cpp
# int process(string &S, string &T, int ss, int se, int ts, int te){
#     if (ts > te){return 1;}
#     int i;
#     int res = 0;
#     for (i = ss; i < se - (te - ts)+1; i++){
#         if (T[ts] == S[i]){res += process(S, T, i+1, se, ts + 1, te);}
#     }
#     return res;
# }
# process(S, T, 0, S.size()-1, 0, T.size()-1);
# ```

# S 是母串, T 是子串; s 就是 start 的意思, e 是 end 的意思, ss 、 se 、 ts 、 te 意思自然明白了
# 递归过程如下:
# 1. 递归返回条件为: 如果 ts > te, 说明子串已经全部匹配完, 所以返回 1, 算一种情况
# 2. 对于母串, 从 ss 下标开始, 一直到(ss - (te - ts) + 1)下标结束, 其中 te-ts+1 为子串的长度
# 3. i 遍历母串的每一个初始位置, 如果 T[ts] == S[i], 说明第一个字符匹配了, 继续进入递归过程, res 累加记录每次的结果, 最后返回
##################################################################
# 这里的暴力递归显然有很多的重复计算, 所以我们可以通过记忆化的方式, 将结果先保存下来,
#     仔细观察上面的递归函数, 只有参数 ss 和 ts 在变化, 所以可以用一张二维的表记录下每组 ss 和 ts 对应的值, 以后直接查表即可
