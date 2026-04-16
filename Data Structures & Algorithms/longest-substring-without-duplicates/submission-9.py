'''
use set to keep track of the current chars in our string

If we find a character in in the set, that means we have repeating character, and we need to move l
up and remove all chars in the set until we are able to add teh char at r to the set.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        mx = 0
        l = 0
        for r,c in enumerate(s):
            if c in chars:
                while c in chars:
                    mx = max(mx, r - l)
                    chars.remove(s[l])
                    l+= 1
            chars.add(c)
            mx = max(mx, r - l+ 1)
        return mx