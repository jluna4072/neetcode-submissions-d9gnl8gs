class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        first, last = 0, len(matrix[0]) - 1
        row = -1
        while top <= bot:
            m = (top + bot)//2
            if matrix[m][first] > target:
                bot = m - 1
            elif matrix[m][last] < target:
                top = m + 1
            else:
                row = m
                break
        if row == -1:
            return False

        l,r = first, last
        while l <= r:
            m = (l+r)//2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m- 1
            else:
                l = m + 1
        
        return False
                




        
