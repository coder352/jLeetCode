#!/usr/bin/python
# coding: utf-8

##################################################################
# 题目  88ms 比 8ms 的 c++ 慢
##################################################################
# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000,
# and there exists one unique longest palindromic substring.

##################################################################
# 解题
##################################################################


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return 0
        maxLen = 1
        start = 0
        for i in xrange(len(s)):
            if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:  # python 这里用的太方便了
                start = i - maxLen - 1  # 奇变奇 偶变偶 单个字母算是回文, 然后就从3个开始, 所以 >= 1
                maxLen += 2
                continue

            if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
                start = i - maxLen  # 奇变偶 偶变奇 单个字母是回文, 从2个开始查找, 所以 >= 0
                maxLen += 1
        return s[start:start + maxLen]

if __name__ == '__main__':
    str = 'helaloabccbaworld'
    res = Solution()
    print res.longestPalindrome(str)
