class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pick = nums[0]
        count = 0

        for n in nums:
            if n != pick:
                count -= 1
            else:
                count += 1
            
            if count <= 0:
                pick = n
        return pick