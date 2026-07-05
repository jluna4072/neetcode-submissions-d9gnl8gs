# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        nth = head
        cur = head
        cnt = n
        while cnt > 0 and cur:
            cur = cur.next
            cnt-= 1
        
        while cur:
            cur = cur.next
            prev = nth
            nth = nth.next
        if prev:
            prev.next =nth.next
            return head

        if nth.next == None:
            return None

        
        return head.next

    
    '''
    1,2
    n
        c
    '''
    
