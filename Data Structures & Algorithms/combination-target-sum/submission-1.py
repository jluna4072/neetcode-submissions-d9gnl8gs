class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        numset = set()
        subset = []
        sum = [0]
        n = len(nums)
        def dfs(i):
            
            if sum[0] == target:
                copy = subset.copy()
                if tuple(copy) not in numset:
                    res.append(subset.copy())
                numset.add(tuple(subset.copy()))
            
            if sum[0] > target or i >= n:
                return

            subset.append(nums[i])
            sum[0] += nums[i]
            dfs(i)

            num = subset.pop()
            sum[0] -= num
            dfs(i + 1)
        
        dfs(0)
        return res

            

            

