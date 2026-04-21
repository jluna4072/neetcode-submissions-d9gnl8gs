'''
Use a map to keep frequency of each letter in s1.
Use another map to keep frequency of each letter in a window the SIZE of s1 in s2

We can use a sliding window approach, where the window is of size s1. 

As we move the window, we want to keep trakc off the freuqnecyof each window. If both maps are ever
equal, they is a subset that is a permutation


lecabee
 l
  r
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        s2_map = defaultdict(int)
        l = 0
        if len(s2) < len(s1):
            return False
        for r in range(len(s2)):
            s2_map[s2[r]] += 1
            if r - l + 1 < len(s1):
                continue
            if s2_map == s1_map:
                return True
            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:
                del s2_map[s2[l]]
            l+= 1
        return False
