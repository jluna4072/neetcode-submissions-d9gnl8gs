class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = float("-inf")

        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            return (1 + dfs(r + 1, c) +
                dfs(r - 1, c) + 
                dfs(r, c - 1) +
                dfs(r, c + 1))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    sm = dfs(r,c)
                    res = max(res, sm)
        
        return res if res != float("-inf") else 0