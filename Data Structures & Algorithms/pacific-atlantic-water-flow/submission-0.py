
'''
we can start from tyeh edges of the boards

set ranges for each ocean:
- Pacific will be [0 - ROWS][0], [0][0 - COLS]
- Atlantic will be [-1][COLS], [ROWS][-1]

We use a visited set to mark the ones we have reached so we dont check cells multiple times

use a matrix outpuit, where each cell has the count of how many oceans have reache dit. If a cell count is 2, then we know that both oceans reach it so we add to res list.


Set ROWS and COLS
set matrix 
set res
set visited
set neighbors

def dfs
    if r or c not it range or in visited or height > parent:
        return
    
    visted add r,c

    for every neighbor direction
        dfs into that neighbor
    
    return



'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]: 
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()
        res = []
        neighbors = [[1,0], [-1,0], [0,-1], [0,1]]
        inf = float("-inf")

        def dfs(r, c, visit, prev):
            if (r not in range(ROWS) or
                c not in range(COLS) or 
                heights[r][c] < prev or 
                (r,c) in visit
                ):
                return

            visit.add((r,c))
            
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visit, heights[r][c])
            
            return
        
        #Pacific
        for r in range(ROWS):
            dfs(r, 0, pac, inf)
            dfs(r, COLS-1, atl, inf)

        for c in range(COLS):
            dfs(0, c, pac, inf)
            dfs(ROWS-1, c, atl, inf)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res 
