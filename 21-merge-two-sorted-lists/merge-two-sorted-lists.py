# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1 = list1
        curr2 = list2
        prev=head =ListNode(0)
        
        while curr1 and curr2 :
            if curr1.val < curr2.val:
                prev.next = curr1
                prev= curr1
                curr1 = curr1.next
            else:
                prev.next = curr2
                prev= curr2
                curr2 = curr2.next

        if curr1:
            prev.next = curr1
        else:
            prev.next = curr2
        head = head.next
        return head


            