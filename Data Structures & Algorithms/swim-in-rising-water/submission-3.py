'''
We can use dikstras to always to towards the smallest possible path (the path that has the shallowest water)

The heap will store [t, (r,c)], so it will pop the path with the lowest time waited at the point. 

We will calculat eth time waited by looking at the current time at that point, and the distanc eof the path so far. If teh time is greater than the distance, then wecarry that time until the time is less than the distance. At every point basically, we update that paths time with the current nodes height, unless the height is lower.

WE will keep a visit set to keep track of all the nodes we have already visited. If we have laready visited a node, we know we already found the fastest path to get to it. 

when we reach grid[-1][-1], we return the t at that point. 


visit set
neighbors, in this case [[1,0], [0,1]]
min_heap

while the min_heap:
    pop t, r, and c from heap
    if r,c is bottom right:
        return max(t,grid[-1,-1])
    visit.add(r,c)
    for dr and dc in neighbor:
        nr nc
        if nr nc not in visit and grid[nr,nc] >= time:
            heap push ((max(t,grid[nr,nc]),(r,c)))
'''

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit = {0,0}
        neighbors = [[1,0],[-1,0],[0,-1], [0,1]]
        min_heap = [(grid[0][0],0, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if r == ROWS -1  and c == COLS - 1:
                return t
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if ((nr,nc) not in visit and
                    nr in range(ROWS) and
                    nc in range(COLS)
                ):

                    heapq.heappush(min_heap, (max(t,grid[nr][nc]), nr, nc))
                    visit.add((nr,nc))
        
        return -1


        '''
        heap: (0,0,0)

        
        
        '''








