class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=None
        c=head
        while c:
            temp=c.next
            c.next=p
            p=c
            c=temp
        return p
