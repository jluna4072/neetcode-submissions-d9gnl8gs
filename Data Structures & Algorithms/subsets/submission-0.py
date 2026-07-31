class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(i, arr, n):
            if i >= n:
                res.append(arr.copy())
                return
            
            #inclue
            arr.append(nums[i])
            dfs(i + 1, arr, n)

            #exclude
            arr.pop()
            dfs(i + 1, arr, n)

        
        dfs(0, [], n)
        return res

            

