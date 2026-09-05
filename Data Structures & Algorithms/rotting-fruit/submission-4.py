
'''
Input: You are given a 2-D matrix grid. Each cell can have one of three possible values:

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit

Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Output: Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1

multi-source BFS:
Find how many total fruits are in the gird
Find how ma ny rotten fruit there is, then add to queue

start from the rotting fruit going outwards, keeping track of the minutes each level.
Use visited set to keep track of visited cells for efficiency

Get fruits
Get rotten fruits add to queue
set neighbors
create minutes

while queue is not empty
    for len of queue
        pop rotten from queue
        for direc in neighbors
            if cell is fruit and not rotten or empty
                aDD neighbor off rotten fruit to queue, mking it rotten now
                make that cell == 2 now
                subtract from total amunt of fresh fruit
    add one to minutes

return minutes if the count of fruits is zero, otherqise -1

'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fruit = 0
        q = deque()
        minutes = 0
        neighbors = [[1,0], [-1,0], [0,1], [0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fruit += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        if fruit == 0:
            return 0
        
        while fruit and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS) and 
                        nc in range(COLS) and
                        grid[nr][nc] == 1):

                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fruit-= 1
            
            minutes+= 1
        
        return minutes if not fruit else -1

        '''
        q = [(0,1)]
        fruit = 1

        [[1,1,0],
        [0,2,2],
        [0,2,2]]
        '''

                








        