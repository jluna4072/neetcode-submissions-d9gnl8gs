class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            cur = {}
            for c in s:
                cur[c] = cur.get(c,0) + 1
            key = tuple(sorted(cur.items()))
            res.setdefault(key, []).append(s)
        
        return list(res.values())