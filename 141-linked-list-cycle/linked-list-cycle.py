# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # #BF 
        # hashset = set()
        # curr =head
        # while curr:
        #     if curr in hashset:
        #         return True
        #     else:
        #         hashset.add(curr)
        #     curr = curr.next
        # return False
        # time O(n)
        # space O(N)
        if head is None or head.next == None:
            return False
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
            
        return False
        # time O(n)
        # space O(1)