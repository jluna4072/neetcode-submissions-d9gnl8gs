import math
'''
Input: piles, where the ith element represents a pile of bananas
        h, number of hours we have to eat all piles

We can eat k bananas per hour. Each our, we can choose a pile and eat k banasas from it,
if the bananas are less than k, we cant eat fro another pile within the same hour

Goal: Return teh min int k that I can eat all bananas within h hours


The MIN number of bananas we can eat per hour is one. We can do binary search on
the rang of hours (1-9). this represents our k

We then iterate throught the array, getting the cieleing division of the piles by k,
and adding to a varibale to track hours. If it is less than or equal
h, we check if its the min seen so far, otherwise we ignore since it has to be
within h

1,1,1,999999999
min = 5
l = 1, r = 499999999

k = 500000000


'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx_pile = max(piles)
        l, r = 1, mx_pile
        res = 0
        while l <= r:
            k = (l+r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
            
