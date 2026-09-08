'''
Dffs from all the edges. 
- If we 'O': We mark all os connected to this one with a '.'

from this, we iterate through all cells at thet end and replace any 'O', with 'X', and any '.' with 'O'

'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        neighbors = [[1,0], [-1,0], [0,-1], [0,1]]

        def dfs(r,c):
            if (r not  in range(ROWS) or
                c not in range(COLS) or 
                board[r][c] == 'X' or
                board[r][c] == '.'
            ):
                return
            
            if board[r][c] == 'O':
                board[r][c] = '.'
            
            for dr, dc in neighbors:
                nr, nc = r+dr, c+dc
                dfs(nr, nc)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)
        
        for c in range(COLS):
            dfs(ROWS - 1, c)
            dfs(0, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '.':
                    board[r][c] = 'O'



    