# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1->2->3->4
        2->1->4->3
        
        curr : 1
        curr : 2->3->4
        curr : 2->1->3->4
        """
        if not head or not head.next:
            return head
        temp = head.next
        head.next = self.swapPairs(head.next.next)
        temp.next = head
        return temp