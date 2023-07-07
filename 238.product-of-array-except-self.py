#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for i in nums:
            prod*=i
        ans = []
        for idx,i in enumerate(nums):
            if i!=0:
                val = prod/i
            else:
                val = 1
                for id2,j in enumerate(nums):
                    if not idx == id2:
                        val*=j

            ans.append(val)
        return list(map(int,ans))
        
# @lc code=end

