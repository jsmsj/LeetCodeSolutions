#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List
class Solution:

    def choose_3(self,ls):
        combos = []
        for i in range(len(ls)):
            for j in range(len(ls)):
                for k in range(len(ls)):
                    if i!=j and i!=k and j!=k:
                        x = sorted([i,j,k])
                        if x not in combos:
                            combos.append(x)
        final = []
        for m in combos:
            i,j,k = m
            final.append([ls[i],ls[j],ls[k]])
        return final




    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        z = self.choose_3(nums)
        # print(z)
        for i in z:
            if sum(i) == 0:
                dd = sorted(i) 
                if dd not in ans:
                    # print(i)
                    ans.append(dd)
        return ans



print(Solution().threeSum([34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
))

# @lc code=end

