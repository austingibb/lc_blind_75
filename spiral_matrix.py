class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
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
