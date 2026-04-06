class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
            Do not return anything, modify nums1 in-place instead.
        10,20,10,20,20,40
    i      l
        1,2
          j
        """

        l = len(nums1) - 1
        i,j = m - 1, n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[l] = nums1[i]
                i-= 1
            else:
                nums1[l] = nums2[j]
                j-=1
            l-= 1
        
        if i < 0:
            while j >= 0:
                nums1[l] = nums2[j]
                j-= 1
                l-= 1
        elif j < 0:
            while i >= 0:
                nums1[l] = nums1[i]
                i-= 1
                l-= 1

        