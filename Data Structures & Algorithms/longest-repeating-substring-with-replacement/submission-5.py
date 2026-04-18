'''
AAAAABBBBCBB
L
       R
MF = A
rep = 4


We use sldiing window approach. As we exxpand, keep track of teh most frequent charactyer seen so far. (get (r - l) - map[mf] and if its 
greater than k we hrink the window, keeping tracvk of who the new mf is.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = 0
        mc = -1
        longest = 0
        for r, c in enumerate(s):
            freq[c]+= 1
            mc = max(mc, freq[c]) 
            
            while (r- l + 1) - mc > k:
                freq[s[l]]-= 1
                l+= 1
            longest = max(longest, r - l + 1)
        return longest
