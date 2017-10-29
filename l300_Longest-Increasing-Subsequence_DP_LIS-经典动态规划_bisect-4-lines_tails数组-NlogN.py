#!/usr/bin/python3
# coding: utf-8
##################################################################
## Description
# Given an unsorted array of integers, find the length of longest increasing subsequence.
# For example,
#     Given [10, 9, 2, 5, 3, 7, 101, 18],
#     The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
#     Note that there may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test cases.
##################################################################
## 耐心排序法: time O(NlogN), Space O(N); 详细解释: [SegmentFault](https://segmentfault.com/a/1190000003819886)
# 思路:
# 在 1,3,5,2,8,4,6 这个例子中, 当到 6 时, 我们一共可以有四种
# (1) 不同长度
# (2) 且保证该升序序列在同长度升序序列中末尾最小
# 的升序序列
#
# 1
# 1,2
# 1,3,4
# 1,3,5,6
# 这些序列都是未来有可能成为最长序列的候选人. 这样, 每来一个新的数, 我们便按照以下规则更新这些序列
#
# 如果 nums[i] 比所有序列的末尾都大, 或等于最大末尾, 说明有一个新的不同长度序列产生, 我们把最长的序列复制一个, 并加上这个 nums[i].
# 如果 nums[i] 比所有序列的末尾都小, 说明长度为 1 的序列可以更新了, 更新为这个更小的末尾.
# 如果在中间, 则更新那个末尾数字刚刚大于等于自己的那个序列, 说明那个长度的序列可以更新了.

# 比如这时, 如果再来一个 9, 那就是第三种情况, 更新序列为
# 1
# 1,2
# 1,3,4
# 1,3,5,6
# 1,3,5,6,9

# 如果再来一个 3, 那就是第二种情况, 更新序列为
# 1
# 1,2
# 1,3,3
# 1,3,5,6

# 如果再来一个 0, 那就是第一种情况, 更新序列为
# 0
# 1,2
# 1,3,3
# 1,3,5,6

# 前两种都很好处理, O(1) 就能解决, 主要是第三种情况, 实际上我们观察直到 6 之前这四个不同长度的升序序列, 他们末尾是递增的,
#     所以可以用二分搜索来找到适合的更新位置.
# 注意
# 二分搜索时如果在 tails 数组中, 找到我们要插入的数, 也直接返回那个结尾的下标, 虽然这时候更新这个结尾没有意义, 但少了些判断简化了逻辑
##################################################################
## Solution: O(nlogn);
# tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i].
# For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:
#     len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
#     len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
#     len = 3   :      [4, 5, 6]            => tails[2] = 6
# We can easily prove that tails is a increasing array. Therefore it is possible to do a binary search in tails array to find the one needs update.
# Each time we only do one of the two:
#     (1) if x is larger than all tails, append it, increase the size by 1
#     (2) if tails[i-1] < x <= tails[i], update tails[i]
# Doing so will maintain the tails invariant. The the final answer is just the size.
class Solution:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)  # 这里只存储 每个不同长度序列 的最后一位
        size = 0  # 表示最长的一个序列的长度
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x: i = m + 1
                else: j = m
            # 上面这一段 i, j 是为了定位 x 在 tails[] 中的位置
            tails[i] = x
            size = max(i + 1, size)
        return size
print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(Solution().lengthOfLIS([4,2,4,5,3,7]))  # 4
##################################################################
## Use bisect; 将上面进行简化
class Solution:
    def lengthOfLIS(self, nums):
        import bisect
        minend = [float('inf')] * (len(nums) + 1)  # minend[i] is the minimum ending of an increasing subsequence of length i+1
        for num in nums:
            minend[bisect.bisect_left(minend, num)] = num
        return minend.index(float('inf'))  # 找到第一个 inf, 好厉害...
print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(Solution().lengthOfLIS([4,2,4,5,3,7]))  # 4
##################################################################
## 动态规划法: time O(N^2), Space O(N)
# 由于这个最长上升序列不一定是连续的, 对于每一个新加入的数, 都有可能跟前面的序列构成一个较长的上升序列, 或者跟后面的序列构成一个较长的上升序列
# 比如 1,3,5,2,8,4,6, 对于 6 来说, 可以构成 1,3,5,6, 也可以构成 2,4,6
#     因为前面那个序列长为 4, 后面的长为 3, 所以我们更愿意 6 组成那个长为 4 的序列, 所以对于 6 来说, 它组成序列的长度
#     实际上是之前最长一个升序序列长度加 1, 注意这个最长的序列的末尾是要小于 6 的, 不然我们就把 1,3,5,8,6 这样的序列给算进来了
# 这样, 我们的递推关系就隐约出来了, 假设 dp[i] 代表加入第 i 个数能构成的最长升序序列长度,
#     要在 dp[0] 到 dp[i-1] 中找到一个最长的升序序列长度, 又保证序列尾值 nums[j] 小于 nums[i], 然后把这个长度加上 1 就行了
#     同时, 我们还要及时更新最大长度
class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums: return 0
        dp, ans = [1] * len(nums), 1
        for i in range(1, len(nums)):
            dp[i] = max([dp[j]+1 for j in range(i) if nums[i] > nums[j]] + [1])  # + [1] 只是为了保证 max() 里面不是空的...
            ans = max(ans, dp[i])
        return ans
print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(Solution().lengthOfLIS([4,2,4,5,3,7]))  # 4
