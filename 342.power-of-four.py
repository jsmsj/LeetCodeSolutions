#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
from math import log10,trunc
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <=0:
            return False
        a = log10(n)/log10(4)
        return float(trunc(a)) == a
        
# @lc code=end

