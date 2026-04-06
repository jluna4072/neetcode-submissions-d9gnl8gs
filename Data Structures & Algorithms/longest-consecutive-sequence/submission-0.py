class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in nums:
            cur_length = 0
            if n-1 not in num_set:
                cur_n = n
                while cur_n in num_set:
                    cur_length+= 1
                    cur_n+= 1
            longest = max(longest, cur_length)
        
        return longest
