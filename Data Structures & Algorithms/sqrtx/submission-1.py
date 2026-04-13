class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        
        while l<= r:
            m = (l+r)//2
            sqr = m*m
            if sqr == x:
                return m
            elif sqr < x:
                l = m + 1
            else:
                r = m - 1
        return r
