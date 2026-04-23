'''
we can have 2 maps, one for t, and one to eep count of teh freq of 
each window in s of size t.

To know if each window of s has all letters need from t, we can use a counter that keeps
track of the letters we need. If we add a letter, and it has teh same frequency, we add
to this counter. once the counter is the same size as the map t, we know we have all needed
letters.

We can then begin to shrink the window from the left side. As we delte, we check if that 
letter is in t. After deleting it, we check if it still has teh required amount of that letter.
if not, we decrese counter, therefore we expand more.
accounted for
Iteratre through s (l and r)
    s_map[s[r]] += 1
    if s[r] in tmap, and the freq == needed:
        counter += 1
    
    #start decreasing window
    if counter == len(t_map):
        if cur len is less than min len:
            min len = cur
            res string = substring
        if s[l] in tmap[]:
            coutner -= 1
        -= 1 for freq of s[l]
        if its 0, we delete form map
OUZODYXAZV
l
        r    

return 
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = Counter(t)
        s_dict = defaultdict(int)
        min_len  = float("inf")
        res = ""
        l = r = 0
        counter = 0
        if len(t) > len(s):
            return ""
        
        while r < len(s):
            s_dict[s[r]]+= 1
            if s[r] in t_dict and s_dict[s[r]] == t_dict[s[r]]:
                counter += 1
            
            while counter == len(t_dict):
                if r - l + 1< min_len:
                    min_len = r - l + 1
                    res = s[l:r + 1]
                if s[l] in t_dict and s_dict[s[l]] == t_dict[s[l]]:
                    counter -= 1
                s_dict[s[l]] -= 1
                if s_dict[s[l]] == 0:
                    del s_dict[s[l]]
                l+= 1
            
            r+= 1

        while l <= r and counter == len(t_dict):
            if r - l < min_len:
                min_len = r - l 
                res = s[l:r ]
            if s[l] in t_dict and s_dict[s[l]] == t_dict[s[l]]:
                counter -= 1
            s_dict[s[l]] -= 1
            if s_dict[s[l]] == 0:
                del s_dict[s[l]]
            l+= 1

        return res

                
