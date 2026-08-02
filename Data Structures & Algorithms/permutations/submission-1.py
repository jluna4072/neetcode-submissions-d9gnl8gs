class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = []
        res = []
        def dfs(pick):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    dfs(pick)
                    perm.pop()
                    pick[i] = False

        dfs([False] * len(nums))
        return res
            