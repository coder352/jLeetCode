#!/usr/bin/python
# coding: utf-8
##################################################################
## Description; 124ms 挺快的
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
##################################################################
## Solution
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):  # type nums1: List[int]; type nums2: List[int]; rtype: float
        nums1.extend(nums2)
        a = sorted(nums1)
        if len(a) % 2 == 0: r = float(float(a[len(a) / 2 - 1] + a[len(a) / 2]) / 2.0)
        else: r = a[len(a) // 2]
        return r
if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    res = Solution()
    print(res.findMedianSortedArrays(nums1, nums2))
