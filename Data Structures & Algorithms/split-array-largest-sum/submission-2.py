'''
2,4,10,1,5

1,0,2,3,5


res
'''
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(mx):
            sm = 0
            res = 0
            large = float("-inf")
            for n in nums:
                sm+= n
                if sm == mx:
                    res+= 1
                    large = max(large, sm)
                    sm = 0
                elif sm > mx:
                    res+= 1 
                    large = max(large, sm - n)
                    sm = n
            
            if sm:
                res += 1
                large = max(large, sm)
            if res <= k:
                return (True, large)
            return (False, float("inf"))
        
        
        l, r = 1, sum(nums)
        min_larg = float("inf")
        while l <= r:
            m = (l+r)//2
            res = canSplit(m)
            if res[0]:
                min_larg = min(min_larg, res[1])
                r = m - 1
            else:
                l = m + 1
        return min_larg
