#!/usr/bin/python
# coding: utf-8

##################################################################
# 题目
##################################################################
# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.

##################################################################
# 解题 162ms 比 7ms 的java慢了点
##################################################################


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Method One: four lines
        # 等号右面是 一个三元判别式, 记录最长的
        # 将一行换为两行,因为两个数赋值没有先后顺序,所以会错
        l_substr, l_suffix = '', ''
        for each in s:
            # l_suffix, l_substr = each in l_suffix and l_suffix[l_suffix.index(each) + 1:] + each or l_suffix + each, max((l_suffix, l_substr), key=len)
            l_suffix = each in l_suffix and l_suffix[l_suffix.index(each) + 1:] + each or l_suffix + each
            l_substr = max((l_suffix, l_substr), key=len)
        return len(l_substr)

if __name__ == '__main__':
    # str = "abcabcbb"
    str = 'au'
    res = Solution()
    print res.lengthOfLongestSubstring(str)
