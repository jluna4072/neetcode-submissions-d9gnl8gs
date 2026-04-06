'''
[1,2]
'''
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for c in operations:
            if c == '+':
                temp2 = stack.pop()
                temp1 = stack.pop()
                stack.append(temp1)
                stack.append(temp2)
                stack.append(temp1 + temp2)
            elif c == 'C':
                stack.pop()
            elif c == 'D':
                temp = stack[-1]
                stack.append(temp * 2)
            else:
                stack.append(int(c))
        
        return sum(stack)