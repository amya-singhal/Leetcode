# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        x = []
        while curr:
            x.append(curr.val)
            curr = curr.next
        l = 0
        r = len(x)-1
        while (l < r):
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1
        return True