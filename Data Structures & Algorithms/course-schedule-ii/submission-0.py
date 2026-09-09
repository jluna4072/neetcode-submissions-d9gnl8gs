class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        visit = set()
        cycle = set()
        res = []

        for u, v in prerequisites:
            adj[u].append(v)
        
        def dfs(child):
            if child in visit:
                return True
            if child in cycle:
                return False

            cycle.add(child)

            for node in adj[child]:
                if not dfs(node):
                    return False
            
            cycle.remove(child)
            visit.add(child)
            res.append(child)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res 

