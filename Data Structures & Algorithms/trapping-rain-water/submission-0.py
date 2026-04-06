'''
0,2,0,3,1,0,1,3,2,1 
                l
                  r

We keep track of the max height found for l and r, moving up whichever pointer has the
smallest max

As we move up, we compare to cur max. If its less, we add difference to res, otherwise me make the
the pointer the new max

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l_max = r_max = float("-inf")
        l, r = 0, len(height) - 1

        while l <= r:
            if l_max <= r_max:
                l_max = max(l_max, height[l])
                res += l_max - height[l]
                l+= 1
            else:
                r_max = max(r_max, height[r])
                res += r_max - height[r]
                r-= 1
        
        return res

