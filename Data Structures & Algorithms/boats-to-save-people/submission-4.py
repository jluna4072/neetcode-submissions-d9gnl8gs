# 1,2,2,3,3
#   l
#   r
#boats = 3

# 



class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l,r = 0, n-1
        boats = 0
        while l<=r:
            if l == r:
                boats+= 1
                break
            total = people[r] + people[l]
            if total <= limit:
                l+= 1
                r-= 1
            else:
                if people[l]>= people[r]:
                    l+= 1
                else:
                    r-= 1
            boats += 1
        return boats
            