# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, r = head, head
        while True:
            if not r or not r.next or not r.next.next:
                return None
            l = l.next
            r = r.next.next
            if l == r:
                break
        l = head
        while l != r:
            l = l.next
            r = r.next
        return l
        