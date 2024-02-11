# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0, head)
        currL = head
        prev = dummy
        while left > 1:
            prev = currL
            currL = currL.next
            left -= 1
            right -= 1
        prevR = currL
        currR = currL.next
        while right > 1:
            tmp = currR.next
            currR.next = prevR
            prevR = currR
            currR = tmp
            right -= 1
        currL.next = currR
        prev.next = prevR
        return dummy.next
        
        
        
            
        