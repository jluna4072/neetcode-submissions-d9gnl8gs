# # -3,0,1,2,3,3
#    l 
#            r
#      l1
#          r2


    

# -2,-1,0,0,1,2
# l         
#             r
   
# -3,-1,0,2,4,5 
# l
#             r
#      l1
#         r2

# cur = -
# total =    

'''
We use two pointers to get the sum of two lef tna dright elements
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l,r = j+ 1, n- 1
                while l< r:
                    sm = nums[i] + nums[j] + nums[l] + nums[r]
                    if sm == target:
                        res.append([nums[i], nums[l], nums[r], nums[j]])
                        l+= 1
                        r-= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif sm < target:
                        l+= 1
                    else:
                        r-= 1
                    
        return res










