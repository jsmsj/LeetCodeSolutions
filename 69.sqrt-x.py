#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0,1]:
            return x
        
        num = x
        g1 = x/2
        
        while True:
            g2 = (g1 + num/g1)/2
            if abs(g2*g2 - num) < 0.00001:
                return int(g2)
            
            g1 = g2
        
# @lc code=end

