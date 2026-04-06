class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1,2,0
        l
            r
          i
        """
        def swap(j,i):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        def sort(nums):
            l,r = 0, len(nums) - 1
            i = 0
            while i <= r:
                if nums[i] == 0:
                    swap(l,i)
                    l+=1
                elif nums[i] == 2:
                    swap(r,i)
                    r -= 1
                    i-=1
                i += 1
        
        sort(nums)



        