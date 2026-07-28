class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for x, y in points:
            heapq.heappush(heap, (math.sqrt((0 - x)**2 + (0 - y)**2), [x, y]))
        
        res = []
        while k > 0:
            dist, point = heapq.heappop(heap)
            res.append(point)
            k-= 1
        
        return res
            