class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        subset = []
        res = []

        def backtrack(i, sm):
            if sm == target:
                res.append(subset.copy())
                return
            
            if i >= n or sm > target:
                return
            
            subset.append(candidates[i])
            backtrack(i + 1, sm + candidates[i])
            num = subset.pop()

            while i + 1 < n  and candidates[i] == candidates[i + 1]:
                i+= 1

            backtrack(i + 1, sm)

            return
        
        backtrack(0,0)
        return res


            