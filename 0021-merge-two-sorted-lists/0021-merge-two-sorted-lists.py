# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        ans = ListNode(0)
        final = ans
        while list1 and list2:
            tmp = 0
            if list1.val < list2.val:
                tmp = list1.val
                list1 = list1.next
            else:
                tmp = list2.val
                list2 = list2.next
            ans.next = ListNode(tmp)
            ans = ans.next
        if list1:
            ans.next = list1
        if list2:
            ans.next = list2
        return final.next
            
        