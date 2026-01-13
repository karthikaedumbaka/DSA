# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        for _ in range(n):
            curr = curr.next
        sec_curr = head
        prev= None
        while curr:
            prev = sec_curr
            sec_curr = sec_curr.next
            curr= curr.next
        if prev:
            prev.next = prev.next.next
            return head
        else:
            return head.next


        