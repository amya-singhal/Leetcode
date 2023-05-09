# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        x = []
        prev = None
        curr = head
        while (curr):
            x.append(curr.val)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        q = 0
        while(prev):
            if (prev.val != x[q]):
                return False
            else:
                prev = prev.next
                q += 1
        return True