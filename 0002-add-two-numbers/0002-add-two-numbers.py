# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        2->4->3
        5->6->4
        outputLinkedList:
        tmp = 2+5 = 7
        carryOn = 0
        outputLinkedlist : 7
        tmp = 4 + 6 + carryOn = 10 -> 0
        carryOn = 1
        outputLinkedlist = 7->0
        tmp = 3+4+carryOn = 8
        carryOn = 0
        outputLinkedList = 7->0->8
        return outputLinkedList
    
        output: 8->9->9->9
        carryOn = 1
        tmp = 9 + carryOn = 10->0
        carryOn = 1
        output : 8->9->9->9->0
        carryOn = 1
        output : 8->9->9->9->0->0
        carryOn = 1
        output : 8->9->9->9->0->0->0
        carryOn = 1
        output : 8->9->9->9->0->0->0->1 
        """
        tmp1 = l1
        tmp2 = l2
        c1 = 0
        c2 = 0
        while(tmp1):
            c1 += 1
            tmp1 = tmp1.next
        while(tmp2):
            c2 += 1
            tmp2 = tmp2.next
        if (c1 > c2):
            currL = l1
            currS = l2
        else:
            currL = l2
            currS = l1
        dummy = currL
        carryOn = 0
        while(currS):
            x = currL.val + currS.val + int(carryOn)
            carryOn = 0
            if (x >= 10):
                carryOn = x / 10
                x =  x % 10
            currL.val = x
            currL = currL.next
            currS = currS.next
        
        while(currL):
            x = currL.val + int(carryOn)
            carryOn = 0
            if (x >= 10):
                carryOn = x / 10
                x =  x % 10
            currL.val = x
            currL = currL.next
        newHead = dummy
        if carryOn != 0:
            while(newHead):
                if (newHead.next == None):
                    tmp = ListNode(1)
                    newHead.next = tmp
                    break
                newHead = newHead.next
        
        return dummy
                
        
        
            
        
        
        
        
        
        
        
        