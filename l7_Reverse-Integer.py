#!/usr/bin/python
# coding: utf-8
##################################################################
## Description
# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# Have you thought about this? Here are some good questions to ask before coding.
# Bonus points for you if you have already thought through this!
#
# If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
#
# Did you notice that the reversed integer might overflow?
# Assume the input is a 32-bit integer, then the reverse of 1000000003
# overflows. How should you handle such cases?
#
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#
# Update (2014-11-10):
# Test cases had been added to test the overflow behavior.
##################################################################
## Solution 解题 68ms  java 2ms
class Solution(object):
    def reverse(self, x):  # :type x: int; :rtype: int
        a = int(str(x)[::-1]) if x >= 0 else -self.reverse(-x)  # 递归调用
        return a if a < 2**31 - 1 else 0  # 这里就会把 负值的过滤为 0
if __name__ == '__main__':
    n = 1234567
    n = -1234567
    res = Solution()
    print(res.reverse(n))
print("test len")
print(len(str(2 ** 31)))
print(2 ** 31)
print(len('1000000003'))
