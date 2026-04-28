# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            while len(stack) and stack[-1] < curr.val:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next
        
        dummay = ListNode()
        curr = dummay
        for v in stack:
            curr.next = ListNode(v)
            curr=curr.next
        return dummay.next
        #time O(n)
        #space O(n)

        