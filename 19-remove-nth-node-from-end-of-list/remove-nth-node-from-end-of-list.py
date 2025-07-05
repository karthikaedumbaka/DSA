# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head: Optional[ListNode]) -> int:
        ans = 0 
        curr = head
        while curr:
            ans += 1
            curr = curr.next
        return ans

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length_list = self.length(head)
        if n == length_list:
            temp = head
            head = head.next
            del temp
            return head
        curr = head

        for i in range(length_list - n -1):
            curr=curr.next
        temp = curr.next
        curr.next=curr.next.next
        del temp 
        return head


    # time O(n)
    # space O(1)
        
        