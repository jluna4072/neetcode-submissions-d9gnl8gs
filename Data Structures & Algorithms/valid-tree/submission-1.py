'''
badcially, if we find any loops, it is not a vlaid tree

a node must not have an edge between another node unless its its parent or child, it cant be another deeper acnestor
'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for child in adj[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False

            return True 
        
        return dfs(0, - 1) and len(visited) == n
        
        

