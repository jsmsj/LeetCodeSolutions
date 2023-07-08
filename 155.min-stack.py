#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.ds = []
        

    def push(self, val: int) -> None:
        self.ds.append(val)
        

    def pop(self) -> None:
        self.ds.pop()
        

    def top(self) -> int:
        return self.ds[-1]
        

    def getMin(self) -> int:
        return min(self.ds)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(55)
# obj.push(-5)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

