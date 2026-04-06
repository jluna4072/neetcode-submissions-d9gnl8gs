class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = re.sub('[^a-zA-Z0-9]', '', s)
        new = new.lower()
        l = 0 
        r = len(new)-1
        while l<=r:
            if new[l] != new[r]:
                return False
            r-=1
            l+=1
        return True