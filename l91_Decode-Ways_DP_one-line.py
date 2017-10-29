#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#     'A' -> 1
#     'B' -> 2
#     ...
#     'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
# For example,
#     Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#     The number of ways decoding "12" is 2.
##################################################################
## Solution: one-line
class Solution:
    def numDecodings(self, s):
        from functools import reduce
        # return reduce(lambda (v, w, p), d: (w, (d>'0')*w + (9<int(p+d)<27)*v, d), s, (0, s>'', ''))[1] * 1  # Python3 中不支持 lambda 中用 tuple
        return reduce(lambda x, d: (x[1], (d>'0')*x[1] + (9<int(x[2]+d)<27)*x[0], d), s, (0, s>'', ''))[1] * 1
print(Solution().numDecodings('12'))
##################################################################
## 解释上面的一行
class Solution:
    def numDecodings(self, s):
        v, w, p = 0, int(s>''), ''
        for d in s:
            v, w, p = w, (d>'0')*w + (9 < int(p+d) < 27)*v, d  # (d>'0') 是对 10, 20 这些可以计算, 但 0, 30 这种有错误的, w 直接置为 0
        return w
print(Solution().numDecodings('12'))
print(Solution().numDecodings('0'))  # 0; at a certain point i, if the char is '0' then it must be combine with char i-1,
# w tells the number of ways
# v tells the previous number of ways
# d is the current digit
# p is the previous digit
