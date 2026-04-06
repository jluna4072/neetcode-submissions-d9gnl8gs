class NumMatrix:
    '''
    We need to add a new row at the topa dn column to the left.

    the prefix[i][j] will be equal to prefix[i][j-1] + prefix[i-1][j]

    '''
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        
        self.prefix_matrix = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.prefix_matrix[r][c + 1]
                self.prefix_matrix[r + 1][c + 1] = prefix + above



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottom_left = self.prefix_matrix[r2][c1-1]
        top_left = self.prefix_matrix[r1-1][c1-1]
        top_right = self.prefix_matrix[r1-1][c2]
        bottom_right = self.prefix_matrix[r2][c2]
        return bottom_right - top_right - bottom_left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)