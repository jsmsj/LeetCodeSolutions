#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+', '-', '*','/']
        
        for i in tokens:
            if i in operations:
                one = stack.pop()
                two = stack.pop()
                if i == '/':
                    stack.append(int(float(two)/float(one)))
                else:
                    stack.append(eval(f"{two}{i}{one}"))
            else:
                stack.append(i)
        # print(stack)
        return int(stack[0])
    
# Solution().evalRPN(["18"])
        
# @lc code=end

