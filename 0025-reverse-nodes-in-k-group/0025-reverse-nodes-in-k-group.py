# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        times = count // k
        curr = head
        prev_node = dummy = ListNode()
        dummy.next = head
        curr = head
        while times:
            prev = prev_node.next
            for i in range(k):
                if curr:
                    t = curr.next
                    curr.next = prev
                    prev = curr
                    curr = t
                else:
                    break
            prev_node.next.next = curr
            temp_head = prev_node.next
            prev_node.next = prev
            prev_node = temp_head
            times -= 1
        return dummy.next
                
                
                
                
        