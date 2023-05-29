# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(0, head)
        prev = dummy
        while (left>1):
            prev = curr
            curr = curr.next
            left -= 1
            right -=1
        # prev will stay with us
        
        x1 = curr
        x = curr
        y = curr.next
        while(right>1):
            tmp = y.next
            y.next = x
            x = y
            y = tmp
            right -= 1
        prev.next = x
        x1.next = y
        return dummy.next
        