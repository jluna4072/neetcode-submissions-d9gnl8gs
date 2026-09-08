'''
Create an adjacenct list: prereq[0] -> re[1]

then we iterate from 0 - numCourses, doing dfs on each course

we keep track of the courses weve seen through a visited set.

If we are iterating through the courses, and the c is already in the visited se
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        visited = set()
        for c, pre in prerequisites:
            adj[c].append(pre)
        
        def dfs(c):
            if c in visited:
                return False
            
            if not adj[c]:
                return True

            visited.add(c)
            for pre in adj[c]:
                if not dfs(pre):
                    return False

            visited.remove(c)
            adj[c] = []

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True


'''
0 ->  1 -> 2
       <-
'''