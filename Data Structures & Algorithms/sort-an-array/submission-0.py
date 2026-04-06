class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            left = arr[l:m+1]
            right = arr[m+1:r+1]
            i, k, j = l, 0, 0

            while k < len(left) and j < len(right):
                if left[k] <= right[j]:
                    arr[i] = left[k]
                    k += 1
                else:
                    arr[i] = right[j]
                    j += 1
                i += 1
            
            while k < len(left):
                arr[i] = left[k]
                k += 1
                i += 1
            
            while j < len(right):
                arr[i] = right[j]
                j += 1
                i += 1
            
        def mergeSort(arr, l , r):
            if l>= r:
                return
            m = (l + r) // 2

            #left side
            mergeSort(arr, l, m)
            
            #right side
            mergeSort(arr, m + 1, r)

            merge(arr, l, m, r)

        mergeSort(nums, 0, len(nums)-1)
        return nums
                    