# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        head = [1,2,3,4,5], n = 2
        
        head = [1,2] n= 2
        length = 2
        index = 0
        """
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        if length == 1 or length-n == 0:
            return head.next
        index = length-n
        
        curr = head
        i = 1
        while i < index:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        return head
        
        
        