class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(l,r, count):
            while l<=r:
                while l < r and not s[l].isalnum():
                    l+= 1
                while r > l and not s[r].isalnum():
                    r-= 1
                
                if s[r] != s[l]:
                    if count > 0:
                         return False
                    count+= 1
                    left = palindrome(l+1,r, count)
                    right = palindrome( l,r - 1, count)
                    return left or right
                l+= 1
                r-= 1
            return True
        
        return palindrome(0, len(s) - 1, 0)
        