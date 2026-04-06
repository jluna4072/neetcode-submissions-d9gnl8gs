class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(l,r, count):
            while l<=r:
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
        