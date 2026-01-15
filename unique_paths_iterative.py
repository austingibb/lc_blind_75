from collections import deque

class Solution:
    # Works because you always need the left and above tiles to get all unique paths the robot can take to this point
    # left tile is always available because second for loop goes left to right
    # top tile is always available becauase first for loop goes top to bottom (prior row is already filled when current is calculating)
    #
    # each tile represents the number of unique paths until that point, thus to calculate a new tiles
    # number of unique paths the only places it can be entered from by the robot are left and above.
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0] * n for _ in range(m)]
        f[0][0] = 1
        for i in range(0, m):
            for j in range(0, n):
                if i: # not in first row
                    f[i][j] += f[i-1][j]
                if j: # in in first column
                    f[i][j] += f[i][j-1]
        
        return f[-1][-1]
