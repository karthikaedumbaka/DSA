# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curry = 0
        dummy = curr_dummy =ListNode()
        while l1 or l2 or curry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + curry
            curry = total //10 

            curr_dummy.next = ListNode(total % 10)
            curr_dummy = curr_dummy.next

            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
        return dummy.next
            
             
        