from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1

        idx_to_unique_paths = []
        for i in range(0, m):
            idx_to_unique_paths.append([])
            for j in range(0, n):
                idx_to_unique_paths[i].append(-1)

        pos_queue = deque()
        idx_to_unique_paths[m-1][n-1] = 1

        for neighbor in self.get_neighbors(m-1, n-1, m, n, idx_to_unique_paths):
            pos_queue.append(neighbor)

        while len(pos_queue) != 0:
            pos = pos_queue.popleft()
            self.visit(pos, m, n, pos_queue, idx_to_unique_paths)

        self.print_grid(m, n, idx_to_unique_paths)
        return idx_to_unique_paths[0][0]

    def visit(self, pos, m, n, pos_queue, idx_to_unique_paths):
        i, j = pos[0], pos[1]
        if idx_to_unique_paths[i][j] != -1:
            return
        # print("visiting (" + str(i) + ", " + str(j) + ")")
        idx_to_unique_paths[i][j] = self.get_val(i+1, j, m, n, idx_to_unique_paths) + self.get_val(i, j+1, m, n, idx_to_unique_paths)
        for neighbor in self.get_neighbors(i, j, m, n, idx_to_unique_paths):
            pos_queue.append(neighbor)
    
    def is_valid_position(self, i, j, m, n):
        # print("valid pos", "i", i, "j", j, "m", m, "n", n)
        return 0 <= i < m and 0 <= j < n
        
    def get_val(self, i, j, m, n, idx_to_unique_paths):
        # print("get_val", "i", i, "j", j, "m", m, "n", n)
        if self.is_valid_position(i, j, m, n):
            return idx_to_unique_paths[i][j]
        else:
            return 0

    def get_neighbors(self, i, j, m, n, idx_to_unique_paths):
        neighbors = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
        return [neighbor for neighbor in neighbors if self.is_valid_position(neighbor[0], neighbor[1], m, n)]

    def print_grid(self, m, n, idx_to_unique_paths):
        for i in range(0, m):
            for j in range(0, n):
                print(idx_to_unique_paths[i][j], end=" ")
            print()
