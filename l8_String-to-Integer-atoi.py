#!/usr/bin/python
# coding: utf-8
##################################################################
## Description
# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases.
# If you want a challenge, please do not see below and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely
# (ie, no given input specs). You are responsible to gather all the input requirements up front.
#
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see
# your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
#
# spoilers alert... click to show requirements for atoi.
#
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
# and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the
# integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not
# a valid integral number, or if no such sequence exists because
# either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
# If the correct value is out of the range of representable values,
# INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
##################################################################
## Solution 100ms  java: 3ms   c++: 4ms
class Solution(object):
    def myAtoi(self, str):  # type str: str; rtype: int
        import re
        if re.match("[ ]*[-+]?\d+", str):  # match 从行首开始
            r = re.search("(-?\d+)", str)  # search 不用从行首开始
            if r: return max(-2**31, min(2**31 - 1, int(r.group(1))))
        return 0
if __name__ == '__main__':
    str = '1234'  # 1234
    str = '   '  # 0
    str = '123agd'  # 123
    str = '12 34'  # 12
    str = 'ad123'  # 0
    str = '-123'  # -123
    str = '  123'  # 123
    str = '+123'  # 123
    res = Solution()
    print(res.myAtoi(str))
    print(2**31 - 1)
    print(-2**31)
