# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        h  = []
        for i in range(len(lists)):
            if lists[i] == None:
                continue
            heappush(h, (lists[i].val, i))
            lists[i] = lists[i].next
        if not h:
            return None
        ansList = ListNode()
        dummy = ansList
        while(h):
            # print(dummy)
            x, y = heappop(h)
            if lists[y]:
                heappush(h, (lists[y].val, y))
                lists[y] = lists[y].next
            ansList.val = x
            if h:
                ansList.next = ListNode()
                ansList = ansList.next
        return dummy
        
            
            
            