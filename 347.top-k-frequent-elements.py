#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        intmap  ={}
        for i in nums:
            if i in intmap:
                intmap[i] +=1
            else:
                intmap.update({i:1})
        ml  = list(intmap.items())
        def mfn(item):
            return item[1]
        ml.sort(key=mfn,reverse=True)
        topk = ml[:k]
        return [i[0] for i in topk]
        
# @lc code=end

