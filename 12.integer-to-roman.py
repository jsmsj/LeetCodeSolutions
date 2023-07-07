#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:

    def ones_place(self,num:int):
        if num in [1,2,3]:
            return 'I'*num
        elif num == 4: 
            return 'IV'
        elif num in [5,6,7,8]:
            return 'V' + 'I'*(num-5)
        elif num == 9:
            return 'IX'
        else:
            return ''
    
    def tens_place(self,num:int):
        if num in [1,2,3]:
            return 'X'*num
        elif num == 4: 
            return 'XL'
        elif num in [5,6,7,8]:
            return 'L' + 'X'*(num-5)
        elif num == 9:
            return 'XC'
        else:
            return ''
        
    def hundredths_place(self,num:int):
        if num in [1,2,3]:
            return 'C'*num
        elif num == 4: 
            return 'CD'
        elif num in [5,6,7,8]:
            return 'D' + 'C'*(num-5)
        elif num == 9:
            return 'CM'
        else:
            return ''
    
    def thousands_place(self,num:int):
        if num in [1,2,3]:
            return 'M'*num
        else:
            return ''

    def intToRoman(self, num: int) -> str:
        strn = list(map(int,list(str(num))))
        if len(strn) == 1:
            return self.ones_place(num)
        elif len(strn) == 2:
            # print(1)
            return self.tens_place(strn[-2]) + self.ones_place(strn[-1])
        elif len(strn) == 3:
            return self.hundredths_place(strn[-3]) + self.tens_place(strn[-2]) + self.ones_place(strn[-1])
        elif len(strn) == 4:
            return self.thousands_place(strn[-4]) + self.hundredths_place(strn[-3]) + self.tens_place(strn[-2]) + self.ones_place(strn[-1])
            
# print(Solution().intToRoman(58))
        
# @lc code=end

