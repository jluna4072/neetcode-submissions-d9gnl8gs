'''
Create an adjacenct list: prereq[0] -> re[1]

then we iterate from 0 - numCourses, doing dfs on each course

we keep track of the courses weve seen through a visited set.

If we are iterating through the courses, and the c is already in the visited se
'''

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

#         adj = defaultdict(list)
#         visted = set()
#         for c, pre in prerequisites:
#             adj[c].append(pre)
        
#         def dfs(c, visited):
#             if c in visited:
#                 return False
            
#             if not adj[c]:
#                 return True

#             visited.add(c)
#             for pre in adj[c]:
#                 if not dfs(pre, visited):
#                     return False
#             visited.remove(c)
#             return True
        
#         for c in range(numCourses):
#             if not dfs(c, set()):
#                 return False
        
#         return True
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


'''
0 ->  1 -> 2
       <-
'''