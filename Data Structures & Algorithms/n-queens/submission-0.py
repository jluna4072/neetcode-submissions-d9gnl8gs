'''
Goal: return the possible bopards that contain n amount of queens where no queens can attack eachother. A cvan can attack horizontally, vertically, ort diagonally in all directions. 

Idea: We can have two fucntions, one to ac†ually backtrack through the board, and one to check if the queen placement is valid. If it is validf, we continue to backtrack. We can use a visitied set for each place a queen has gone. this allows us at everypoint to check if we can even place it iun a aspecific spot, since if a spot is visited, we know that we cannot place a qwueen there. 
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        neighbors = [[-1, 1], [-1, -1], [-1, 0], [0, -1], [0, 1], [1, -1], [1, 1], [1,0]]
        def markNeighbors(row, col, visited):
            for r in range(ROWS):
                for c in range(COLS):
                    if r == row or c == col or abs(r - row) == abs(c - col):
                        visited.add((r,c))

        def solve(board, visited, row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
                
            for col in range(COLS):
                if (row,col) not in visited:
                    new_visited = visited.copy()
                    board[row][col] = 'Q'
                    markNeighbors(row, col, new_visited)
                    solve(board, new_visited, row+1)
                    board[row][col] = '.'
            
            return

        solve(board, set(), 0)    
        return res