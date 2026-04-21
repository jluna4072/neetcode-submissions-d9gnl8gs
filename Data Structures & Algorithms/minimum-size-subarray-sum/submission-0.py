'''
use a variabale sliding window. while the sum of the subbarray is less than target. Once it is 
greater than or equal, we shrink form the left until its less sum


2,1,5,1,5,3

8
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        sm = 0
        res = float("inf")
        while r < len(nums):
            while sm < target and r < len(nums):
                sm += nums[r]
                r+= 1
            while sm >= target:
                res = min(res, r - l)
                sm-= nums[l]
                l+= 1
        
        return res if res != float("inf") else 0

            
