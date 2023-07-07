#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        og = str(x)
        ls =  list(og)
        rev = ''.join(ls[::-1])
        return rev == og

        
# @lc code=end

