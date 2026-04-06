'''
4#love4#neet4#code
  i
      j 
'''

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string = encoded_string + str(len(s)) + '#' + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i= 0
        words = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j+= 1
            n = int(s[i:j])
            i= j + 1
            j+= (n+1)
            words.append(s[i:j])
            i = j
        return words