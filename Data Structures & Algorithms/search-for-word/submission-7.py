'''
backtracking:
matrix dfs

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        neighbors = [[-1, 0], [1,0], [0, -1], [0, 1]]
            
        def dfs(i, r, c, used):
            if word[i] != board[r][c]:
                return False
            
            if i == len(word) - 1:
                return True
            
            found = False
            used.add((r, c))
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in used:
                    if dfs(i + 1, nr, nc, used):
                        found = True
                        break

            used.remove((r,c))
            return found 
        
        for r in range(ROWS):
            for c in range(COLS):
                if word[0] == board[r][c]:
                    if dfs(0, r, c, set()):
                        return True
        
        return False
                    

            
