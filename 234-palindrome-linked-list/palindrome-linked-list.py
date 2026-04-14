from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse_data = deque([])
        curr = head
        while curr:
            reverse_data.appendleft(curr.val)
            curr= curr.next
        i = 0 
        curr = head
        while curr:
            if reverse_data[i] != curr.val:
                return False
            curr = curr.next
            i+=1
        return True
        
        