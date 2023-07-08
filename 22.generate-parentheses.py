#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # notes: only add `)` if open count > close count
        # stop when open = close = n
        # max open < n
        stack = []
        ans = []

        def recurse(open,close):
            if open == close == n:
                ans.append(''.join(stack))
                return
            if open < n:
                stack.append('(')
                recurse(open+1,close)
                stack.pop()
            
            if close < open:
                stack.append(')')
                recurse(open,close+1)
                stack.pop()

        recurse(0,0)

        return ans
        


        




# @lc code=end

