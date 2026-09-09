'''
We can do dfs from every single node. We keep track of visited ones in a set

iterate from 0 -n, calling dfs on each. We check if the node has already been visited, if it has, then it is already a ap of a connected component. Like number of islands, but for adjacency list


'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        visited = set()
        components = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for con in adj[node]:
                dfs(con)
            
            return
        
        for node in range(n):
            if node in visited:
                continue
            dfs(node)
            components+= 1

        return components 
        