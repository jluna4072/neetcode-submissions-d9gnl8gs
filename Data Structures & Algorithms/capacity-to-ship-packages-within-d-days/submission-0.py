'''
Use the max wieght found in array as our min, and the sum of all weights as our max
for binary search. 

Witht the mid range, we use a greedy approach to see if we can take all weights. If we 
cant do it in the days, we move the total capacty up, lese, we save and move it down.

1,5,4,4,2,3

11

min = 12

'''

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Computes if capacity is valid
        def canShip(capacity):
            rolling = 0
            d = 0
            for w in weights:
                rolling+= w
                if rolling == capacity:
                    d+= 1
                    rolling = 0
                elif rolling > capacity:
                    d+= 1
                    rolling = w
            if rolling:
                d+= 1
            if d > days:
                return False
            return True
                    

        min_capacity = float("inf")
        l, r = max(weights), sum(weights)

        while l <= r:
            m = (l + r)//2
            if canShip(m):
                min_capacity = min(min_capacity, m)
                r = m - 1
            else:
                l = m + 1
        return min_capacity
    
    