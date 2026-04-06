'''
use stack to check if asteroid collide.

If our curr n is negative, we loop through top of stack and while the top is less than
the abs of the num, we pop. If it finds one equal, we pop and continue, 
and if the top is greater, we continue

if its positive, we just add to stack


stack = [8, ]

for every asteroid:
    if the asteroid is going left:

'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a < 0:
                broken = False
                while stack and stack[-1] > 0:
                    if stack[-1] >= abs(a):
                        if stack[-1] == abs(a):
                            stack.pop()
                        broken = True
                        break
                    else:
                        stack.pop()
                if not broken:
                    stack.append(a)
            else:
                stack.append(a)
        return stack