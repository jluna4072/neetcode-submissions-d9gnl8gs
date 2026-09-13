'''
TWe need to find an edge that makes the graph cyclical, then remove it. 

We can do this with dfs, keeping track of which nodes are in visited (ones we visite aooing the way)

We need to keep track of the noes that are a part of a cycle, and all the nodes we visit. If we ever come across a node weve already visited, we add that to the cycle, and when we return from that, if the cycleStart is the last node, then we stop since we know we have gotten all the nodes that are a part of that.


'''
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        cycle = set()
        start = [-1]

        def dfs(node, par):
            if node in visited:
                start[-1] = node
                return True
            
            visited.add(node)
            for neigh in adj[node]:
                if neigh == par:
                    continue
                if dfs(neigh, node):
                    if start[-1] != -1:
                        cycle.add(node)
                    if start[-1] == node:
                        start[-1] = -1
                    return True
                
            return False
        
        dfs(1, -1)
        
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []


