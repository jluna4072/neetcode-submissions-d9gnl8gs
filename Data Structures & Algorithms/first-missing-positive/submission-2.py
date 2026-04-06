'''
-1,-2,-4,-5,-5,3,1

   

1. Iterate through array, making all negative elements 0. This is because
negatives do not matter in the context of this problem.

2. Iterate throught the array again and for every index i, nums[nums[i] - 1] * -1
this is to mark that nums[i] is in the array. If nums[i] - 1 end up being 0, 
we make it equal to len(nums) + 1 * -1

3. We iterate 1 - len(nums) + 1. If nums[i] is not negative, we return i

-1,-2,-4,-5,-6,3,1

j = 1
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            if -1 < j < len(nums) and nums[j] == 0:
                nums[j] = -(len(nums) + 1)
            elif -1 < j < len(nums) and nums[j] > 0:
                nums[j] = nums[j] * -1
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >=0:
                return i
        
        return len(nums) + 1