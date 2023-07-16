# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans=ListNode(0)
        if len(lists)==0:
            return None
        heap=[]
        heapify(heap)
        for l in range(len(lists)):
            if lists[l]:
                heappush(heap, [lists[l].val, l])
        if not heap:
            return None
            
        curr = ans
        while(heap):
            x, y=heappop(heap)
            curr.next = ListNode(0)
            curr = curr.next
            curr.val = x
            if lists[y].next is not None:
                lists[y] = lists[y].next
                heappush(heap, [lists[y].val,y])
            else:
                continue
        return ans.next
        