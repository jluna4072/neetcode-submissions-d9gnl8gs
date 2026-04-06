class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1,2,0
        l
            r
          i
        """
        count = [0] * 3

        for i in range(len(nums)):
            count[nums[i]] += 1
        
        j = 0
        for i in range(3):
            while count[i]:
                nums[j] = i
                j+=1
                count[i]-=1
        



        