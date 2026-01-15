from collections import deque

class Solution:
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