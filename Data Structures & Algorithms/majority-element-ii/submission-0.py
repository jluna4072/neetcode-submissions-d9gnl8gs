class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1

            if len(count) <= 2:
                continue
            
            new_count = {}
            for num, c in count.items():
                if c > 1:
                    new_count[num] = c - 1
            count = new_count
            
                
        res = []
        for num in count:
            if nums.count(num) > len(nums)//3:
                res.append(num)
        return res

        
            