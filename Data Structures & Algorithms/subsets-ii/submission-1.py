'''
1, 1, 2


'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        subset = []
        nums.sort()

        def backtrack(i):
            if i == n:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(i + 1)

            
            subset.pop()
            j = i
            while j + 1 < n  and nums[j] == nums[j + 1]:
                j+= 1
            backtrack(j + 1)
            
            return
        
        backtrack(0)
        return res

        

            
        