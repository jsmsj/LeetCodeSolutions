#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            _max = min(i+k,len(nums))
            _min = max(i-k,0)
            for j in range(_min,_max):
                if i!=j and nums[i] == nums[j]:
                    return True
        

            
            
        
        return False
        
# @lc code=end

