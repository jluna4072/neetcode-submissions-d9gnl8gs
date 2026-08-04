'''
1, 1, 2


'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset  = []
        res = []
        n = len(nums)

        def backtrack(i):
            if i == n:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
            j = i
            while j < n - 1 and nums[j] == nums[j+1]:
                j+= 1
            backtrack(j+1)
            return
        
        backtrack(0)
        return res
            
        
        


        

            
        