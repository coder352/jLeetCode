StefanPochmann 跟着大牛走...
### DP Dynamic Programming
``` zsh
# 动态规划的核心: 状态转移方程
# 动态和暴力的区别是: 1. 动态规划用状态转移方程, 暴力是直接枚举所有情况, DP 其实相当于 暴力 + 剪枝
./l368_Largest-Divisible-Subset_4-lines-DP.py  # 这里要保存状态转移过程, 可以有更简单的方法...
./l91_Decode-Ways_DP_one-line.py  # dp[i] = dp[i] + dp[i-1]

./l198_House-Robber_3-lines-DP.py
./l213_House-Robber-II_6-lines-DP.py
./l337_House-Robber-III_Tree-DP.py  # 三个动态 DP 问题的关键是将中间状态用字母表示出来, 然后通过构造状态转移方程, 一步一步的求解

./l121_Best-Time-to-Buy-and-Sell-Stock_reduce-简化为一行_DP-与其他方法对比.py  # reduce 函数写的真好, 还有 DP 思想与正常方法的对比; 只能买一次
./l122_Best-Time-to-Buy-and-Sell-Stock-II_DP_zip-去ij化.py  # sum(zip()) 函数式编程; 可以买无数次
./l123_Best-Time-to-Buy-and-Sell-Stock-III_DP_实现了买一次和买无数次中间的买k次.py  # 更加通用了..., 买 k 次
./l188_Best-Time-to-Buy-and-Sell-Stock-IV_DP_在l123基础上进行剪枝.py  # 有容易超时的数据, 要剪枝
./l309_Best-Time-to-Buy-and-Sell-Stock-with-Cooldown_DP_讲解的非常详细-注重过程的思考.py  # ** 一定要把这个看了 **, 这个很重要

./l115_Distinct-Subsequences_DP-Matrix_Space-optimization_暴力递归-动态规划.py  # 空间优化和不优化进行对比
# 暴力递归 -> 剪枝(记忆化搜索) -> 动态规划 -> 空间压缩优化的动态规划;
# 想起了算法课第一次作业中的 分割多边形为三角形 多少种方法, 原来也是一个动态规划的题目...; 当时还纠结复杂度是 O(n!)
./l128_Longest-Consecutive-Sequence_DP_但是没用动态规划.py  # 本来是一个 DP 题, 却可以用 暴力 更快
./l674_Longest-Continuous-Increasing-Subsequence_DP_简单的连续递增子串.py  # 没有用 DP 和 使用 DP 对比, 很简单
./l300_Longest-Increasing-Subsequence_DP_LIS-经典动态规划_bisect-4-lines_tails数组-NlogN.py  # ** 从 N^2 到 NlogN **
./l673_Number-of-Longest-Increasing-Subsequence_DP.py  # 和 l300 很像, 但是没有了 NlogN 的时间复杂度
# Leetcode 上有人说 l673 有 NlogN 的解...
./l491_Increasing-Subsequences_DP_set-在用list生成器的感觉.py  # 也没用 DP, 直接暴力所有的子序列

./l131_Palindrome-Partitioning_DP_一行暴力递归-动态规划.py  # 这个是典型的用空间换时间, 动态规划的思想好勉强的...
./l132_Palindrome-Partitioning-II_DP_不能一行写出来.py  # 尝试使用一行将 DP 写出来, 失败了, 必须记录中间状态, 不是直接生成 列表...
```
