#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List
class Solution:
    def isvaliditem(self,item):
        if set(item) == {"."}:
            return True
        rmap = {}
        for i in item:
            if i == ".":
                continue
            if i in rmap:
                rmap[i]+=1
            else:
                rmap.update({i:1})
        return set(rmap.values()) == {1}


    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # mm = set([
        #     board[i][j] for i in range(9) for j in range(9)
        # ])
        # if  mm == {"."}:
        #     return True

        for row in board:
            x = self.isvaliditem(row)
            # print(x)
            if not x:
                return False
            
        # print()
            
            
        cols = [
            [board[i][j] for i in range(9)] for j in range(9)
        ]
        
        for col in cols:
            x = self.isvaliditem(col)
            # print(x)
            if not x:
                return False
            
        # print()

        boxes  = [
            
            [board[i][j] for i in range(3) for j in range(3)],
            [board[i][j] for i in range(3) for j in range(3,6)],
            [board[i][j] for i in range(3) for j in range(6,9)],

            [board[i][j] for i in range(3,6) for j in range(3)],
            [board[i][j] for i in range(3,6) for j in range(3,6)],
            [board[i][j] for i in range(3,6) for j in range(6,9)],

            [board[i][j] for i in range(6,9) for j in range(3)],
            [board[i][j] for i in range(6,9) for j in range(3,6)],
            [board[i][j] for i in range(6,9) for j in range(6,9)],
        ]
        
        for box in boxes:
            x = self.isvaliditem(box)
            
            if not x:
                # print(box)
                return False

        return True

# t1 = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
# t2 = [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]


# print(Solution().isValidSudoku(t1))
        
# @lc code=end

