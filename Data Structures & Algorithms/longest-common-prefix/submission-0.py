class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_word = min(w for w in strs)
        for i,c in enumerate(min_word):
            for word in strs:
                if word[i] != c:
                    return word[0:i] 
        return min_word
            