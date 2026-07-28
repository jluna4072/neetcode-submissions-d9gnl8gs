class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) > 1:
            x = heapq.heappop_max(heap)
            y = heapq.heappop_max(heap)
            smash = abs(x-y)
            if smash > 0:
                heapq.heappush_max(heap, smash)
        if not heap:
            return 0
        return heap[0]