class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        neighbors = [[-1, 0], [1,0], [0, -1], [0,1]]
        dist = 0
        while q:
            for _ in range(len(q)):

                row, col = q.popleft()
                if ((row,col) in visited or row not in range(ROWS) or col not in range(COLS)
                    or grid[row][col] == -1 ):
                    continue 
                
                visited.add((row,col))
                grid[row][col] = dist
                for dr, dc in neighbors:
                    nr, nc = row + dr, col + dc
                    q.append((nr, nc))
            dist+= 1
        
        
                
                
            