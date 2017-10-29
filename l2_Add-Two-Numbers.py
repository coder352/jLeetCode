#!/usr/bin/python
# coding: utf-8
##################################################################
## Description
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and
# each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
##################################################################
## Solution
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# copy here
class Solution:  # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        res = n = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            n.next = n = ListNode(val)
        return res.next
if __name__ == '__main__':
    l1 = tmp = ListNode(2)
    tmp.next = tmp = ListNode(4)
    tmp.next = tmp = ListNode(3)
    l2 = tmp = ListNode(5)
    tmp.next = tmp = ListNode(6)
    tmp.next = tmp = ListNode(4)

    res = Solution()
    tmp = res.addTwoNumbers(l1, l2)
    while tmp:
        print(tmp.val)
        tmp = tmp.next
