'''

'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def dfs(opn, clsd):
            if opn == clsd == n:
                res.append("".join(subset))
                return
            
            if opn < n:
                subset.append("(")
                dfs(opn + 1, clsd)
                subset.pop()

            if clsd < opn:
                subset.append(")")
                dfs(opn, clsd + 1)
                subset.pop()
            
            return
        
        dfs(0, 0)
        return res

        