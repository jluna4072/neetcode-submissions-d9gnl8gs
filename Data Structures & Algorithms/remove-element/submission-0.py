'''
4,3,2,1,1
l 
      r
'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[r] == val:
                r-=1
                continue
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
        
        return l