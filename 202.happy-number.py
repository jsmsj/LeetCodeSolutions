#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def dig_sq_sum(self,n:int):
        s = 0
        for i in list(str(n)):
            s+=int(i)**2
        return s
        
    def isHappy(self, n: int) -> bool:
        cache = []
        m = n
        cache.append(m)
        while 1:
            x = self.dig_sq_sum(m)
            if x == 1:
                return True
            elif x in cache:
                return False
            cache.append(x)
            m = x



# @lc code=end

