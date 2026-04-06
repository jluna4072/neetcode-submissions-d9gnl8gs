class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        the time to get to 'target' is respresentd by
        x = (target - postion[i])/ speed[i]

        since a car cannot pass another car, we can use a monotonic stack to 
        represent each group of cars

        if we find a car at the top of the stack that will take longer to get to the
        target compared to current car, then the current car will become apart of its fleet.

        otherwise, it will get added to the stack
        '''

        stack = []
        cars = sorted(zip(position,speed), reverse = True)
        for pos,speed in cars:
            x = (target - pos) / speed
            if stack and stack[-1] >=x:
                continue
            stack.append(x)
        
        return len(stack)
        
        
        # target=12
        # position=[10,8,0,5,3]
        # speed=[2,4,1,1,3]

        # stack[1,12]