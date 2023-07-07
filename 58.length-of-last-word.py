#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
import re
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        patt = re.compile(r'\s+')
        return len(patt.sub(' ',s).split(' ')[-1])

        
# @lc code=end

