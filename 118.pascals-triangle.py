#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
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

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            ans.append([self.ncr(i,j) for j in range(i+1)])
        return ans

        
# @lc code=end

