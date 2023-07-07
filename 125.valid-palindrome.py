#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = string.printable.replace('abcdefghijklmnopqrstuvwxyz','').replace('0123456789','')
        s = s.lower()
        for cha in list(chars):
            s = s.replace(cha,'')
        # print(s)
        return s == ''.join(list(s)[::-1])


# print(Solution().isPalindrome('0P'))

# @lc code=end

