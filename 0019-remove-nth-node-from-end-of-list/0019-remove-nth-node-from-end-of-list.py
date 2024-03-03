# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        head = [1,2,3,4,5], n = 2
        
        head = [1,2] n= 2
        length = 2
        index = 0
        """
        def recur(node, prev, index):
            nonlocal head
            if node == None:
                return 0
            index = recur(node.next, node, index)+1
            
            if index == n:
                if node.next == None or prev == None:
                    if prev:
                        prev.next = node.next
                    else:
                        head = node.next
                else:
                    prev.next = node.next
            return index
        curr = head
        index = recur(curr, None, 0)
        return head
        