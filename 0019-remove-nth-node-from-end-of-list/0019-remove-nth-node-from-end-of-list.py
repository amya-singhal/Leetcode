# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        head = [1,2] n= 2
        length = 2
        index = 0
        """
        
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        if length == 1 and n == 1:
            return None
        index = length-n
        i = 1
        curr = head
        dummy = curr
        if index == 0:
            return dummy.next
        while i < index:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        return dummy
        
        
        