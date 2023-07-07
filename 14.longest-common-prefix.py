#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp_ls = [{j[i] for j in strs } for i in range(len(min(strs, key=len)))]
        for idx,v in enumerate(temp_ls):
            if len(v) != 1:
                x = [list(temp_ls[i])[0] for i in range(idx)]
                ans = ''.join(x)
                return ans
        
        return ''.join([list(i)[0] for i in temp_ls])        




# @lc code=end

