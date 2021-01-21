class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        
        p1Prev = None
        p1 = l1
        p2 = l2
        
        while p1 and p2:
            if p1.val <= p2.val:
                p1Prev = p1
                p1 = p1.next
            else:
                if p1Prev:
                    p1Prev.next = p2
                p1Prev = p2
                p2 = p2.next
                p1Prev.next = p1
                
        if p2:
            p1Prev.next = p2
            
        return l1 if l1.val <= l2.val else l2
        