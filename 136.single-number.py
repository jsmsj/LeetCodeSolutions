#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = {}
        for i in nums:
            if i in m:
                m[i] +=1
            else:
                m.update({i:1})
        for i,j in m.items():
            if j == 1:
                return i
        
# @lc code=end

