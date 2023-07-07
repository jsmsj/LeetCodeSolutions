#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        deduped = list(set(nums))
        return len(nums) != len(deduped)

        
# @lc code=end

