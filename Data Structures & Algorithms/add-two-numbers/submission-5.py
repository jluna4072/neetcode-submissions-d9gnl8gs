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
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + carry
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        

        return dummy.next
            
            


        