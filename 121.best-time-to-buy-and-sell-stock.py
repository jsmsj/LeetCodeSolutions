#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) in [0,1]:
            return 0
        buy_at = prices[0]
        profit = 0
        for val in prices[1:]:
            if val < buy_at:
                buy_at = val
            elif val - buy_at > profit:
                profit = val-buy_at
            
        return profit

            


# Solution().maxProfit([7,6,4,3,1])

        
# @lc code=end

