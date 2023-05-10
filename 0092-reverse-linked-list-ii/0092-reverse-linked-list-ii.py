# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:        
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # base case
        if (not head or not head.next):
            return head
        dummy = ListNode()
        dummy.next = head
        prev= dummy
        curr = head
        while(left > 1):
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1
        x1 = curr
        x = curr
        y = curr.next
        while(right > 1):
            tmp = y.next
            y.next = x
            x = y
            y = tmp
            right -= 1 
        prev.next = x
        x1.next = y
        return dummy.next
        
            
        