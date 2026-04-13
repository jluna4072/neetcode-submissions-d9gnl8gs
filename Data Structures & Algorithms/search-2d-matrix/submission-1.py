'''
Input: 2d sorted matrix
Goal: return if a target exists 

First we need to find the row that the target might be in. We can do this by doing binary search on
the rows before columns. If the target is in a row before mid, it is compared with the 
first element of the mid row. Likewise, if it might be greater, it is compared with
last element in the mid. Otherwise, the target is inside of that array.




'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        row = -1
        while top <= bot:
            m = (top + bot)// 2
            if matrix[m][0] > target:
                bot = m - 1
            elif matrix[m][-1] < target:
                top = m + 1
            else:
                row = m
                break

        if row == -1:
            return False

        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            m = (l + r)//2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False

                




        
