#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
from typing import List
class Solution:
    def factorial(self,n):
        if n == 0:
            return 1
        return n*self.factorial(n-1)

    def ncr(self,n,r):
        return int(self.factorial(n)/(self.factorial(r)*self.factorial(n-r)))

    def getRow(self, rowIndex: int) -> List[int]:
        return [self.ncr(rowIndex,j) for j in range(rowIndex+1)]
        
# @lc code=end

