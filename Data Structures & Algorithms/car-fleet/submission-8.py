class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = sorted(zip(position, speed), reverse = True)
        stack = []
        for p, s in position_speed:
            cur = (target - p)/s
            if stack and stack[-1] >= cur:
                continue
            else:
                stack.append(cur)
        return len(stack)

8,6
2,3

stack = [1,]