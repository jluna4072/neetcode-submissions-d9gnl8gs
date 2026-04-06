class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        iterate through string
        if we see a operator: +,-,/, -> pop both values within the expression, and 
        use the operator


        '''
        stack= []
        
        for c in tokens:
            if c == '+':
                num2, num1 = stack.pop(), stack.pop()
                sm = num1 + num2
                stack.append(sm)
            elif c ==  '-':
                num2, num1 = stack.pop(), stack.pop()
                sm = num1 - num2
                stack.append(sm)
            elif c == '/':
                num2, num1 = stack.pop(), stack.pop()
                div = int(num1 / num2)
                stack.append(div)
            elif c == '*':
                num2, num1 = stack.pop(), stack.pop()
                prod = num1 * num2
                stack.append(prod)
            else:
                stack.append(int(c))
        return stack[-1]
