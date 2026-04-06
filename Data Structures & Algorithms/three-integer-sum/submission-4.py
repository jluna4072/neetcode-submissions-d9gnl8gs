'''
-4,-1,-1,0,1,2
         l k r

res[[-1,-1,2],[-1,0,1]]
nums.sort()
l = 0
res = []
for l in range of nums - 1:
    if l == l- 1:
        continu
    k = l + 1
    r = len(nums) - 1
    while k < r:
        sm = nums[l] + nums[k] + nums[r]
        if sm == 0:
            res.append([l,k,r])
            move k up
            move  r down
            while k== k-1:
                move k up
            while r == r+ 1:
                move r down
        elif sm < nums[0]:
            move k up
        else:
            mover r down
return res

-1,-1,0,1
l     k r

        
        
'''
2

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = 0
        res = []
        #So k is never out of range
        for l in range(len(nums) - 1):
            #So we dont find duplicate triplets
            if l > 0 and nums[l] == nums[l-1]:
                continue
            k = l+ 1
            r = len(nums) - 1
            while k < r:
                sm = nums[l] + nums[k] + nums[r]
                if sm == 0:
                    res.append([nums[l],nums[k],nums[r]])
                    k+= 1
                    r-= 1
                    while k < r and nums[k] == nums[k- 1]:
                        k+= 1
                    while r > k and nums[r] == nums[r+ 1]:
                        r-= 1
                elif sm < 0:
                    k+= 1
                else:
                    r-= 1
        return res
            