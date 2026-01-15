class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.spiralOrderOop(matrix)

    def spiralOrderOneFunction(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        
        rows, cols = len(matrix), len(matrix[0])

        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        up_bound = 0
        down_bound = rows
        left_bound = -1
        right_bound = cols
        direction = RIGHT

        result = []

        i, j = 0, 0
        while len(result) < rows * cols:
            if direction == RIGHT:
                while j < right_bound:
                    result.append(matrix[i][j])
                    j += 1
                i, j = i + 1, j - 1
                right_bound -= 1
                direction = DOWN
            elif direction == LEFT:
                while j > left_bound:
                    result.append(matrix[i][j])
                    j -= 1
                i, j = i - 1, j + 1
                left_bound += 1
                direction = UP
            elif direction == DOWN:
                while i < down_bound:
                    result.append(matrix[i][j])
                    i += 1
                i, j = i - 1, j - 1
                down_bound -= 1
                direction = LEFT
            elif direction == UP:
                while i > up_bound:
                    result.append(matrix[i][j])
                    i -= 1
                i, j = i + 1, j + 1
                up_bound += 1
                direction = RIGHT
        
        return result

    def spiralOrderOop(self, matrix: List[List[int]]) -> List[int]:

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        self.direction = Vector(1, 0)
        total_items = len(matrix) * len(matrix[0])
        result = []
        self.matrix = matrix
        self.current_pos = Vector(0, 0)
        self.row_lower = 0
        self.row_upper = len(matrix)
        self.col_lower = -1
        self.col_upper = len(matrix[0])

        iters = 0

        while len(result) != total_items:
            while True:
                result.append(matrix[self.current_pos.y][self.current_pos.x])
                if not self.can_move():
                    break
                self.move()

            self.rotate()
            self.move()

        return result

    def can_move(self) -> bool:
        next_pos = Vector(self.current_pos.x + self.direction.x, self.current_pos.y + self.direction.y)
        if self.direction.x > 0:
            return next_pos.x < self.col_upper
        elif self.direction.x < 0:
            return next_pos.x > self.col_lower
        elif self.direction.y > 0:
            return next_pos.y < self.row_upper
        elif self.direction.y < 0:
            return next_pos.y > self.row_lower

    def move(self):
        self.current_pos.x += self.direction.x
        self.current_pos.y += self.direction.y

    def rotate(self):
        if self.direction.x > 0:
            self.direction.x = 0
            self.direction.y = 1
            self.col_upper -= 1
        elif self.direction.x < 0:
            self.direction.x = 0
            self.direction.y = -1
            self.col_lower += 1
        elif self.direction.y > 0:
            self.direction.x = -1
            self.direction.y = 0
            self.row_upper -= 1
        elif self.direction.y < 0:
            self.direction.x = 1
            self.direction.y = 0
            self.row_lower += 1

    def print_state(self, result):
        print("Dir:", self.direction, "Cur_pos:", self.current_pos, "Row_bounds:", (self.row_lower, self.row_upper), "Col_bounds:", (self.col_lower, self.col_upper), "Result:", result)
