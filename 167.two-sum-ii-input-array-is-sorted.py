#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List
class Solution:

    def find_ele(self,ls,el):
        index= []
        for d,i in enumerate(ls):
            if i == el:
                index.append(d)
        return index

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sol = []
        for idx,i in enumerate(numbers):
            other = target-i
            if other in numbers:
                sol.extend([idx+1,self.find_ele(numbers,other)[-1]+1])
                break
        return sol


        
# @lc code=end

