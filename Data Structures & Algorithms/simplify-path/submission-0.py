'''
Everytime we see a /, we add to stack. If there are mutliple(// or ///), 
we look at the top and while its /, we pop

Once we reach a letter
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = [d for d in path.split("/") if d]
        stack = []

        for dr in dirs:
            if dr == '..':
                if stack:
                    stack.pop()
            elif dr == '.':
                continue
            else:
                new = ["/", dr]
                stack.append("".join(new))
        if not stack:
            stack.append("/")
        return "".join(stack)