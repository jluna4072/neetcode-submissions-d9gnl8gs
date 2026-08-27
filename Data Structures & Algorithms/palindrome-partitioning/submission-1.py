class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        n = len(s)

        def backtrack(i, substrings):
            if i >= n:
                if isPali(substrings[-1]):
                    res.append(substrings.copy())
                return 
            
            if substrings:
                substrings[-1] += s[i]
                backtrack(i + 1, substrings)
                substrings[-1] = substrings[-1][:-1]

            if not substrings or isPali(substrings[-1]):
                substrings.append(s[i])
                backtrack(i + 1, substrings)
                substrings.pop()

            return

        def isPali(st):
            l,r = 0, len(st) - 1
            while l <= r:
                if st[l] != st[r]:
                    return False
                l+= 1
                r-= 1 
            return True 
        
        backtrack(0,[])
        return res