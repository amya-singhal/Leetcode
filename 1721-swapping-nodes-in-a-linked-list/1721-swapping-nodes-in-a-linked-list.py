# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        c = 0
        a = []
        curr = head
        while(curr):
            a.append(curr.val)
            curr = curr.next
            c += 1
        r = c - k
        rM = r
        l = k - 1
        lM = l
        curr2 = head
        x = 0
        while(curr2):
            if rM == x:
                curr2.val = a[lM]
            if lM == x:
                curr2.val = a[rM]
            curr2 = curr2.next
            x += 1
        return head