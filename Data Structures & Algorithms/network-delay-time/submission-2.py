'''
use djisktras algo to get there. 

What we will need:
- heap
- adj list
'''

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((w,v))

        visited = set()
        heap = []
        heapq.heappush(heap, (0, k))

        while heap:
                time , src = heapq.heappop(heap)

                if src in visited:
                    continue 
                
                visited.add(src)

                if len(visited) == n:
                    return time

                for w, v in adj[src]:
                    if v not in visited:
                        heapq.heappush(heap, (w + time, v))
        
        return -1