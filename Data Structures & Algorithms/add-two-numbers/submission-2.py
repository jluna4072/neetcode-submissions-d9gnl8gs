# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
input: two linked lists, each representing an integer
output: sum of the int representation of the two linked lists

Iterate through each list, adding the val of the nodes into a new node. If the sum is doubl digits,
we take the remainder /10, and add it to the next sum. Once we reach the end, if the remainder != 0, 
we add to end
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        n = None
        if l1:
            n = l1
        elif l2:
            n = l2
        while n:
            sum = n.val + carry
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            n = n.next
        
        if carry:
            cur.next = ListNode(carry)
        return dummy.next
            
            


        