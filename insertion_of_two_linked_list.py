def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d1=headA
        d2=headB
        while(d1!=d2):
            if(d1==None):
                d1=headB
            else:
                d1=d1.next
            if(d2==None):
                d2=headA
            else:
                d2=d2.next
        return d1
