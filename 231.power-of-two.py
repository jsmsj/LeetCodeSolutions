#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <=0:
            return False
        a = math.log2(n)
        return float(math.trunc(a)) == a
# @lc code=end

