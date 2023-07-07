#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(0,len(nums)):
            b = target-nums[a]
            if b in nums and a!=nums.index(b):
                return [a,nums.index(b)]
# @lc code=end

