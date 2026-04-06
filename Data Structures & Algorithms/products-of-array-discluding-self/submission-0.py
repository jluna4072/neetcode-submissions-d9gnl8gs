class Solution:
    '''
    [1,2,4,6]

    postfix = 1
    [1,0,0,0]
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res[0] = 1
        
        
        prefix = 1
        for i in range(len(nums)):
            res[i]= prefix
            prefix*= nums[i]
        
        postfix = 1
        for i in range(len(nums)- 1, -1, -1):
            res[i]*= postfix
            postfix*= nums[i]
        
        return res

        