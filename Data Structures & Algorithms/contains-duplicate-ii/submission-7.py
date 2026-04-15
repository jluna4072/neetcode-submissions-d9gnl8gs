class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for i,n in enumerate(nums):
            if n in table:
                if abs(table[n] - i) <= k:
                    return True
            
            table[n] = i
        return False