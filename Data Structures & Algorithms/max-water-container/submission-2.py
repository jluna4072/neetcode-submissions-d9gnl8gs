#the 
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmountWater = float("-inf")
        l,r = 0, len(heights) - 1

        while l < r:
            curMaxHeight = min(heights[l], heights[r])
            distance = r - l
            volume = curMaxHeight * distance
            maxAmountWater = max(maxAmountWater, volume)
            if heights[l] <= heights[r]:
                l+= 1
            else:
                r-= 1
        return maxAmountWater


# 1,7,2,5,12,3,500,500,7,8,4,7,3,6
# l
#                                r
# mx = 13