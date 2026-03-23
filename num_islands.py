class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        if not grid[0]:
            return 0

        return self.num_islands_bfs(grid)

    def num_islands_bfs(self, grid):
        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if self.coord_to_key((i, j)) not in visited and grid[i][j] == '1':
                    self.dfs(grid, i, j, visited)
                    islands += 1
        return islands

    @staticmethod
    def bfs(grid, i, j, visited):
        q = deque((i, j))
        while len(q) > 0:
            i, j = q.pop()
            visited.append(Solution.coord_to_key((i, j)))
            neighbors = Solution.get_neighbors(grid, i, j)
            for neighbor in neighbors:
                if Solution.coord_to_key(neighbor) not in visited:
                    q.appendleft(neighbor)


    def num_islands_dfs(self, grid):
        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if self.coord_to_key((i, j)) not in visited and grid[i][j] == '1':
                    self.dfs(grid, i, j, visited)
                    islands += 1
        return islands
    
    @staticmethod
    def dfs(grid, i, j, visited):
        visited.add(Solution.coord_to_key((i, j)))
        neighbors = Solution.get_neighbors(grid, i, j)
        for i, j in neighbors:
            if Solution.coord_to_key((i, j)) not in visited:
                Solution.dfs(grid, i, j, visited)

    @staticmethod
    def get_neighbors(grid, i, j):
        neighbors = []
        if i - 1 >= 0 and grid[i-1][j] == '1':
            neighbors.append((i-1, j))
        if j - 1 >= 0 and grid[i][j-1] == '1':
            neighbors.append((i, j-1))
        if i + 1 < len(grid) and grid[i+1][j] == '1':
            neighbors.append((i+1, j))
        if j + 1 < len(grid[0]) and grid[i][j+1] == '1':
            neighbors.append((i, j+1))
        return neighbors

    @staticmethod
    def coord_to_key(coord):
        i, j = coord
        return str(i) + " " + str(j)