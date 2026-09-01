class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combos = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(i, sub):
            if len(sub) == len(digits):
                res.append("".join(sub))
                return 
            for c in combos[digits[i]]:
                sub.append(c)
                backtrack(i + 1, sub)
                sub.pop()

        if digits:
            backtrack(0,[])
        return res