class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        numset = set()
        subset = []
        n = len(nums)
        def dfs(i):
            
            if sum(subset) == target:
                copy = subset.copy()
                if tuple(copy) not in numset:
                    res.append(subset.copy())
                numset.add(tuple(subset.copy()))
            
            if sum(subset) > target or i >= n:
                return

            subset.append(nums[i])
            dfs(i)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res

            

            

