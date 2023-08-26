# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        y = head
        while(y and n):
            y = y.next
            n -= 1
        x = dummy
        while(x and y):
            x = x.next
            y = y.next
        if x.next:
            x.next = x.next.next
        return dummy.next
        