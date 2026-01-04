# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        curr =head
        for i in range(k-1):
            curr=curr.next
        left = curr
        right = head
        while curr.next:
            curr=curr.next
            right=right.next
        left.val ,right.val =right.val ,left.val
        return head

        #time O(n)
        #space O(1)
        