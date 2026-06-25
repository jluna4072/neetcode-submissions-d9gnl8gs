# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
One possible solution: trun the linked list into an aray, then do two pointers O(n) time o(n) space
We can do this in O(1) space

We can use fast/slow pointers to get the middle of the linked list. From this points, we can flip
the last half of the array. Then, from the start and the middle, we go left, appending the start pointer
to the linked list first, then the one starting from half

dummy = Listnode
new = dummy.next
fast = slow = cur

while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

cur = slow
prev = null

while cur:
    temp = cur.next
    cur.next = prev
    prev = cur
    cur = temp

cur = head

while cur.val != prev.val:
    new.val = cur.val
    new = new.next
    new.val = prev.val
    new = new.next

return new

'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        cur = slow.next
        slow.next = None
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        first = head
        second = prev
        
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        
            
        