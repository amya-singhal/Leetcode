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
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        while(curr.next and curr.next.next):
            t1 = curr.next
            t2 = curr.next.next
            curr.next, t2.next, t1.next = t2, t1, t2.next
            curr = t1
        return dummy.next