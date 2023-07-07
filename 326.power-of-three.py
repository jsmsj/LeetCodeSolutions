#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
from math import log10,trunc
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <=0:
            return False
        a = log10(n)/log10(3)
        return float(trunc(a)) == a
        
# @lc code=end

