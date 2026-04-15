'''
do binary search. We get the value middle, right, and left

First we find the peak of the array. Tht way we can split the array by that peak, and 
do binary on each side since we know they are in a ascending or descnedng order

We first do it on the left half since we want tot find the leftmost target
We then to the next half. If we dont find any target, we return false

'''

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Find peak of the array.
        
        length = mountainArr.length()
        l,r = 0, length-2
        peak = -1
        while l< r:
            m = (l+r)//2
            if mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1
            else:
                r = m
        peak_i = l

        # Left-side binary search
        l,r = 0, peak_i
        while l<= r:
            m = (l+r)//2
            mid = mountainArr.get(m)
            if mid == target:
                return m
            elif mid < target:
                l= m + 1
            else:
                r= m - 1
        '''

            
        '''
        # RightHand binary search
        l, r = peak_i, length - 1 
        while l<= r:
            m = (l+r)//2
            mid = mountainArr.get(m)
            if mid == target:
                return m
            elif mid > target:
                l= m + 1
            else:
                r= m - 1
        return -1
            
        
        


