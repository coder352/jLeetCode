#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root."
#     Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that
#     "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses
#     were broken into on the same night.
# Determine the maximum amount of money the thief can rob tonight without alerting the police.
# Example 1:
#      3
#     / \
#    2   3
#     \   \
#      3   1
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:
#      3
#     / \
#    4   5
#   / \   \
#  1   3   1
# Maximum amount of money the thief can rob = 4 + 5 = 9.
# Credits:
#     Special thanks to @dietpepsi for adding this problem and creating all test cases.
##################################################################
## Solution
# Let:
#     f1(node) be the value of maximum money we can rob from the subtree with node as root (we can rob node if necessary).
#     f2(node) be the value of maximum money we can rob from the subtree with node as root but without robbing node.
# Then we have:
#     f2(node) = f1(node.left) + f1(node.right) and
#     f1(node) = max(f2(node.left) + f2(node.right) + node.value, f2(node)).  # 这里的 f1(node) 只是两次 f2() 之间的中间变量

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# TreeNode 在 Leetcode 中已经定义好了, 这里不用在生成了
class Solution(object):
    def rob(self, root):  # :type root: TreeNode
        def superrob(node):
            if not node: return (0, 0)  # base case
            left, right = superrob(node.left), superrob(node.right)  # get values
            now = node.val + left[1] + right[1]  # rob now:   max money earned if input node is robbed; 核心是这里的 left[1], right[1], 代表 later
            later = max(left) + max(right)       # rob later: max money earned if input node is not robbed
            return (now, later)
        return max(superrob(root))
# print(Solution().rob([3, 2, 3, null, 3, null, 1]))  # 7; 完全二叉树 的表现形式
#       3
#      / \
#     2   3
#    / \   \
# null 3   1
##################################################################
## Summary:
# 1. 一直以为动态规划不应该有 "暴力递归 + 剪枝" 那种递归, 后来发现 too naive; 碰到了树状数据, gg
