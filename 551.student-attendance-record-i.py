#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
import re
class Solution:
    def checkRecord(self, s: str) -> bool:
        pattA = re.compile(r'A')
        patt = re.compile(r'L{3,}')
        return len(patt.findall(s)) ==0 and len(pattA.findall(s)) <2

     
# @lc code=end

