class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i, n in enumerate(nums):
            need = target - n
            if need in nums_dict:
                return [nums_dict[need], i]
            nums_dict[n] = i
        return []