class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [cnt for cnt in count.values()]
        heapq.heapify_max(maxHeap)

        time = 0
        q = deque()

        while q or maxHeap:
            time += 1
            
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = heapq.heappop_max(maxHeap) - 1
                if cnt: 
                    q.append((cnt, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q[0][0])
                q.popleft()
        
        return time
        
            
