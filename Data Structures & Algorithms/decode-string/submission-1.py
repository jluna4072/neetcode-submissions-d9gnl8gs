'''
2[a3[b]]c

2[a3[b]

we keep pushing sto stack. If we see a clsing bracket, we keep popping from stack 
until we reach opening bracket. We pop one t get rid of it, then we pop the number 
associated wiht the string, and multiply them. We then push back to stack.

'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                string = deque()
                while stack and stack[-1] != '[':
                    string.appendleft(stack.pop())
                stack.pop()
                mult = deque()
                while stack and stack[-1].isdigit():
                    mult.appendleft(stack.pop())
                if mult:
                    mult = int("".join(mult))
                else:
                    mult = 1
                string = "".join(string)
                stack.append(mult*string)
            else:
                stack.append(c)
        return "".join(stack)