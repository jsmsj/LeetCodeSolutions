#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {
            '}':'{',
            ')':'(',
            ']':'['
        }

        for c in s:
            if c in m:
                if len(stack) != 0 and stack[-1] == m[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return False if len(stack)!=0 else True
    
# @lc code=end

