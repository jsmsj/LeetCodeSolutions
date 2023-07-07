#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def toInt(self,num:str):
        s = 0
        for idx,v in enumerate(num[::-1]):
            s+= int(v)* (2**idx)
        return s

    def addBinary(self, a: str, b: str) -> str:
        return bin(self.toInt(a) + self.toInt(b)).replace('0b','')


        
# @lc code=end

