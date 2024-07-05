# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        curr, ans = head, head
        while curr and curr.next:
            tmp = curr.val
            curr.val = curr.next.val
            curr.next.val = tmp
            curr = curr.next.next
        return ans
        