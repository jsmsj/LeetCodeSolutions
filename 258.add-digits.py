#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:

    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        return self.addDigits(sum(list(map(int,list(str(num))))))


# @lc code=end

