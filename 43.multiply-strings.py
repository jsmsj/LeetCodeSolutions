#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def _int(self,num):
        num_sys = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        ls = list(num)[::-1]
        ans = 0
        for idx,val in enumerate(ls):
            ans += num_sys[val] * (10**idx)
        return ans




    def multiply(self, num1: str, num2: str) -> str:
        # print(self._int(num1))
        # print(self._int(num2))
        return str(self._int(num1)*self._int(num2))


# print(Solution().multiply("123","456"))
        
# @lc code=end

