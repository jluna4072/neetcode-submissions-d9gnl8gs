class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def go(tmp, vs):
            did = False
            for i in range(n):
                if not vs[i]:
                    did = True
                    vs[i] = True
                    go(tmp + [nums[i]], vs)
                    vs[i] = False
            if not did:
                return res.append(tmp)
        go([], [False]*n)
        return res
            