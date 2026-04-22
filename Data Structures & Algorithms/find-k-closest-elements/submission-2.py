'''
First do binary search to find where x would be inserted. 

after, we set l to that index, and r to l + 1
from there, we expand out from where it would be inserted. We add the nums[l] first to res
array since it is always going to be less than the right. We can use a deck to properly insert them


do binary search to look for where it should be inserted

We expand form the insertion index
    Check if the index is valid
    For left, if valid, add to list
    for right, if valid, add to list
    l+= 1
    r+= 1
1,3,5,7
    l
      r
    m
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = deque()
        l,r = 0, len(arr) - 1
        i = -1
        while l < r:
            m = (l + r)//2
            if arr[m] < x:
                l = m + 1
            else:
                r = m
        l-= 1
        r = l + 1
        while r < len(arr) or l >= 0:
            if l >= 0 and r >= len(arr):
                res.appendleft(arr[l])
                if len(res) == k:
                        break
                l-= 1
            elif l < 0 and r < len(arr):
                res.append(arr[r])
                if len(res) == k:
                        break
                r+= 1
            else:
                if l >= 0 and r< len(arr) and abs(x - arr[l]) <= abs(x - arr[r]):
                    res.appendleft(arr[l])
                    if len(res) == k:
                        break
                    l-= 1
                elif l >= 0 and r< len(arr) and abs(x - arr[l]) > abs(x - arr[r]):
                    res.append(arr[r])
                    if len(res) == k:
                        break
                    r += 1
        return list(res)



