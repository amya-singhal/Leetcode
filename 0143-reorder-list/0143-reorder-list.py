# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        first = head
        second = head
        while(second.next and second.next.next):
            first = first.next
            second = second.next.next
        curr = first.next
        prev = None
        while(curr):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        first.next = None
        # print(prev)
        # print(head)
        head1 = head
        head2 = prev
        alter = False
        while(head2):
            tmp1, tmp2 = head1.next, head2.next
            head1.next = head2
            head2.next = tmp1
            head1, head2 = tmp1, tmp2
            
            
                
            
            
            
            
        