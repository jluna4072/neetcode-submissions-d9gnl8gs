class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_dict = defaultdict(int)
        prefix_dict[0] = 1
        res = 0
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            target = prefix - k

            res+= prefix_dict[target]
            prefix_dict[prefix] += 1
        
        return res
