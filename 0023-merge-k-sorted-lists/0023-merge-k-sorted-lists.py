# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None:
            return None
        dummy = ListNode(0)
        curr = dummy
        heap = []
        for i in range(len(lists)):
            if lists[i] is None:
                continue
            heapq.heappush(heap, [lists[i].val, i])
            lists[i] = lists[i].next
        print(heap) # [[1,0],[1,1],[2,2]]
        while (heap):
            element, index = heapq.heappop(heap) #1,0
            if lists[index] != None:
                heapq.heappush(heap, [lists[index].val, index])
                lists[index] = lists[index].next
            curr.next = ListNode(element)
            curr = curr.next
        return dummy.next
            