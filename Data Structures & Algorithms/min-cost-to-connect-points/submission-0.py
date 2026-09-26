class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        min_heap = [[0,0]]
        visit = set()
        res = 0
        while len(visit) < len(points):
            dist, p = heapq.heappop(min_heap)
            if p in visit:
                continue
            visit.add(p)
            res += dist
            for neigh_dist, neigh in adj[p]:
                if neigh not in visit:
                    heapq.heappush(min_heap, [neigh_dist, neigh])
        
        return res
                
        

        


        

        
