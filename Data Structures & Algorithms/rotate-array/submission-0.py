class Solution:
    def reverse(self, nums,l, r) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+= 1
            r-= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n == 0 or k == 0:
            return nums
        
        k = k % n

        moved = False
        while not moved:
            self.reverse(nums, 0, n - 1)
            self.reverse(nums, 0, k-1)
            self.reverse(nums, k, n - 1)
            moved = True
        
        return nums

        


