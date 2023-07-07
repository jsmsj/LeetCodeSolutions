#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charmap1 = {}
        for i in s:
            if i in charmap1:
                charmap1[i]+=1
            else:
                charmap1.update({i:1})
        charmap2 = {}
        for i in t:
            if i in charmap2:
                charmap2[i]+=1
            else:
                charmap2.update({i:1})
        return charmap1 == charmap2

# @lc code=end

