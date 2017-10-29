#!/usr/bin/python
# coding: utf-8
##################################################################
## Description
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern
# in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
##################################################################
## Solution 112ms 挺快的  10行
# 解题思路: https://discuss.leetcode.com/topic/54012/python-solution-o-n-with-picture-to-understand
class Solution(object):
    def convert(self, s, numRows):  # :type s: str; :type numRows: int; :rtype: str
        result = [""] * (numRows + 1)
        level, order = 1, 1
        for i in s:
            result[level * order] += i  # 用了 list[-1], 好方便
            level += 1
            if level >= numRows: level, order = 1, order * (-1)
        return "".join(result)
if __name__ == '__main__':
    str = "PAYPALISHIRING"
    n = 3
    res = Solution()
    print(res.convert(str, n))
