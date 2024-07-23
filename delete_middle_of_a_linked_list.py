def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return None
        mid=head
        fast=head
        while fast and fast.next:
            mid=mid.next
            fast=fast.next.next
        temp=head
        while(temp.next!=mid):
            temp=temp.next
        temp.next=mid.next
        return head
