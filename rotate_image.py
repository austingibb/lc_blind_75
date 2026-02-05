class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 0:
            return

        width = n
        while width >= 2:
            row, col = n//2 - width//2, n//2 - width//2

            for i in range(0, width-1):
                self.swap(row, col+i, matrix)
            
            width -= 2

    def swap(self, row, col, matrix):
        val_to_rotate = matrix[row][col]
        for _ in range(0, 4):
            next_row, next_col = self.rotate_coordinate(row, col, matrix)
            overwritten_val = matrix[next_row][next_col]
            matrix[next_row][next_col] = val_to_rotate
            val_to_rotate = overwritten_val
            row, col = next_row, next_col

    def rotate_coordinate(self, row, col, matrix):
        n = len(matrix)
        return col, n - 1 - row
 

def main():
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    s = Solution()
    s.rotate(matrix)

if __name__ == "__main__":
    main()