#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return list(set(range(0,len(nums)+1)) - set(nums))[0]
        
# @lc code=end

