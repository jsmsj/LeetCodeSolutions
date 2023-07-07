#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        details = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        details_edge = {"IX": 9, "IV": 4, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        for k,v in details_edge.items():
            s = s.replace(k,f'|{v}|')
        
        for k,v in details.items():
            s = s.replace(k,f'|{v}|')
        
        return sum(list(map(int,[i for i in s.split('|') if i])))




# @lc code=end
