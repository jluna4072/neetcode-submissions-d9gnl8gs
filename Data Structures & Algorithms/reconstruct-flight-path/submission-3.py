'''
[["HOU","JFK"], ["JFK","HOU"], ["JFK","SEA"], ["SEA","JFK"]]

SEA: JFK
JFK: HOU SEA
HOU: JFK



'''

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        adj = defaultdict(list)

        for u, v in sorted(tickets)[::-1]:
            adj[u].append(v)

        def dfs(src):
            while adj[src]:
                dest = adj[src].pop()
                dfs(dest)
            res.append(src)
        
        dfs("JFK")
        print(res)
        return res[::-1]

