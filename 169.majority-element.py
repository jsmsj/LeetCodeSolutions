#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for i in nums:
            if i in m:
                m[i]+=1
            else:
                m.update({i:1})
        thresh = int(len(nums)/2)
        ls = [[k,v] for k,v in m.items()]
        ls.sort(key = lambda x:x[1],reverse=True)
        for i in ls:
            if i[1] >thresh:
                return i[0]


        
# @lc code=end

