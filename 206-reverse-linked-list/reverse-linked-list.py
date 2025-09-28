# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next   
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev=None
        while curr:
            temp = curr.next
            # temp.next=curr
            curr.next = prev
            prev= curr
            curr = temp
        return prev

    # Time O(N)
    # Space O(1)