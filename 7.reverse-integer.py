#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.45%)
# Likes:    2460
# Dislikes: 3809
# Total Accepted:    807.7K
# Total Submissions: 3.2M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        xReverse = 0
        if x < 0:
            x = -x
            isNegative = True
        while x:
            xReverse = 10*xReverse + x%10
            x = x//10
        if isNegative:
            if xReverse > 2**31:
                return 0
            else:
                return -xReverse
        else:
            if xReverse > 2**31-1:
                return 0
            else:
                return xReverse


