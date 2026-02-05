class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return

        rows, cols = len(matrix), len(matrix[0])

        cols_to_zero, rows_to_zero = [], []

        for col_idx in range(0, cols):
            if Solution.col_has_zero(col_idx, matrix, rows):
                cols_to_zero.append(col_idx)

        for row_idx in range(0, rows):
            if Solution.row_has_zero(row_idx, matrix, cols):
                rows_to_zero.append(row_idx)
        
        for col_idx in cols_to_zero:
            for row_idx in range(0, rows):
                matrix[row_idx][col_idx] = 0
        
        for row_idx in rows_to_zero:
            for col_idx in range(0, cols):
                matrix[row_idx][col_idx] = 0

    def row_has_zero(row_idx, matrix, cols):
        for col_idx in range(0, cols):
            if matrix[row_idx][col_idx] == 0:
                return True
        return False

    def col_has_zero(col_idx, matrix, rows):
        for row_idx in range(0, rows):
            if matrix[row_idx][col_idx] == 0:
                return True
        return False