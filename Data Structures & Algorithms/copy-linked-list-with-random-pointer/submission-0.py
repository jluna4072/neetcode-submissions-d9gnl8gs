"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
'''
use map to keep track of nodes. So, when we reach a node weve crated alrady due to it being another nodes random, 
we can check if it exists already. The key will be the original list node, the value will be the copy
node
'''
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_dict = {None:None}
        cur = head

        while cur:
            copy = Node(cur.val)
            node_dict[cur] = copy
            cur = cur.next
        cur = head
        res = cur
        while cur:
            copy = node_dict[cur]
            copy.random = node_dict[cur.random]
            copy.next = node_dict[cur.next]
            cur = cur.next
        return node_dict[head]
